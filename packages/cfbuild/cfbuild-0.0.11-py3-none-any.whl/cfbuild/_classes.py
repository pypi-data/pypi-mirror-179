import netCDF4
import os
import io

import numpy as np

from importlib import resources
from lxml import etree

from ._create_dataset import from_file
from ._create_ncml import create_ncml
from ._create_nc import create_or_update_nc_file
from ._constants import STANDARD_NAME_TABLE_LOCATION
from ._refresh_ncml import _update_file


class Dataset:
    def __init__(self, dataset_or_filepath: None or str or netCDF4._netCDF4.Dataset = None,
                 conventions: list or str = ['CF-1.9', 'ACDD-1.3']):
        """
        if dataset_or_filepath is netcdf file - read in the file as the Dataset
        if dataset_or_filepath is a netcdf4 dataset - copy as the Dataset
        if dataset_or_filepath is a nonexistant file or an empty file - initiate new Dataset
    
        if write_filepath is None - update to the read_filepath
        

        Parameters
        ----------
        dataset_or_filepath : None or str or netCDF4._netCDF4.Dataset, optional
            DESCRIPTION. The default is None.
        write_filepath : None or str, optional
            DESCRIPTION. The default is None.
        mode : str, optional
            DESCRIPTION. The default is 'strict'.
            Possible Options - strict: includes all 

        Returns
        -------
        None.
        """
        self.attributes = {}
        self.conventions = conventions
        self.crs = None
        self.dataset = None
        self.dimensions = {}
        self.groups = []
        self.read_filepath = None
        self.variables = {}

        with resources.open_binary('cfbuild', STANDARD_NAME_TABLE_LOCATION) as file_path:
            table = file_path.read()

        self.standard_name_table = io.BytesIO(table)

        if type(dataset_or_filepath) == str:
            if os.path.exists(dataset_or_filepath) or dataset_or_filepath[:4] == 'http':
                self.dataset = netCDF4.Dataset(dataset_or_filepath, mode='r')
                self.read_filepath = dataset_or_filepath
                from_file(self)
            else:
                raise FileNotFoundError('file does not exist')
        elif type(dataset_or_filepath) == netCDF4._netCDF4.Dataset:
            self.read_filepath = dataset_or_filepath.filepath()
            self.dataset = dataset_or_filepath
            from_file(self)
        else:
            print('Creating dataset from cfbuild')
            '''
            if self.read_filepath == None:
                print('read filepath not yet set')
            else:
                self.dataset = netCDF4.Dataset(self.read_filepath, mode=write_mode, clobber=clobber)
            '''

    def to_ncml(self, output_filepath: str):
        tree = create_ncml(self)
        tree.write(output_filepath, pretty_print=True)
        new_ncml = NCML(output_filepath, self)
        return new_ncml

    def group(self, name: str):
        new_group = Group(name)
        self.dataset.createGroup(name)
        self.groups.append(new_group)
        return new_group

    def attribute(self, name: str, value: str):
        self.attributes[name] = value

    def variable(self, name: str, data_type: str, dimensions: tuple, variable_type: str or None = None,
                 values: np.array or None = None):
        new_variable = Variable(name, data_type, dimensions, variable_type, values)
        self.variables[name] = new_variable
        return new_variable

    def dimension(self, name: str, length: int or None):
        new_dimension = Dimension(name, length)
        self.dimensions[name] = new_dimension
        return new_dimension

    def crs(self, epsg_number: str or int):
        self.crs = epsg_number
        return epsg_number

    def close(self):
        self.dataset.close()


class Group:
    def __init__(self, name: str):
        self.name = name
        self.attributes = {}
        self.groups = []
        self.variables = []
        self.dimensions = []

    def attribute(self, name: str, value: str):
        self.attributes[name] = value

    def group(self, name: str):
        new_group = Group(name)
        self.groups.append(new_group)
        return new_group

    def variable(self, name: str, data_type: str, dimensions: tuple, variable_type: str or None = None,
                 values: np.array or None = None):
        new_variable = Variable(name, data_type, dimensions, variable_type, values)
        self.variables[name] = new_variable
        return new_variable

    def dimension(self, name: str, length: int or None):
        new_dimension = Dimension(name, length)
        self.dimensions[name] = new_dimension
        return new_dimension


class Variable:
    def __init__(self, name: str, data_type: str, dimensions: tuple, variable_type: list or None = None,
                 values: np.array or None = None):
        self.name = name
        self.data_type = data_type
        self.dimensions = dimensions
        self.values = values
        self.attributes = {}
        self.variable_type = variable_type

    def attribute(self, name: str, value: str):
        self.attributes[name] = value


class Dimension:
    def __init__(self, name: str, length: str or int):
        self.name = name
        self.length = length


class NCML:
    def __init__(self, ncml_filepath: str, dataset: Dataset):
        self.ncml_filepath = ncml_filepath
        self.dataset = dataset  # this is an cfbuild dataset object
        self.xml_tree = etree.parse(ncml_filepath)

    def to_nc(self, nc_filepath: str or None = None, write_mode: str = 'w'):
        """
        Creates an ncml file showing the structure of the netCDF file along with all attributes neccissary to make the 
        file CF compliant. The argument filepath is a path to an .ncml which will be written when the class is created.
        """

        if write_mode == 'clobber':
            write_mode = 'w'
            clobber = True
        else:
            write_mode = 'w'
            clobber = False

        final_netcdf4_dataset = netCDF4.Dataset(nc_filepath, mode=write_mode, clobber=clobber)
        create_or_update_nc_file(self, final_netcdf4_dataset, self.dataset.dataset)
        final_netcdf4_dataset.close()

    def refresh_file(self):
        original_xml_tree = self.xml_tree
        new_xml_tree = etree.parse(self.ncml_filepath)
        _update_file(original_xml_tree, new_xml_tree)
        return self
