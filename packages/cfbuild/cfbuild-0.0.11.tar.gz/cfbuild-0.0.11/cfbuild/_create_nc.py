import numpy
import json

from lxml import etree
from ._constants import VARIABLE_TYPE_INDICATORS


def create_or_update_nc_file(ncml_object, final_netcdf4_dataset, original_dataset):
    def validate_json(json_data):
        try:
            json.loads(json_data)
        except ValueError:
            return False
        return True

    def check_element_for_values(xml_group, variable_shape, dimensions):
        has_values = False
        variable_values = None

        for element in xml_group:
            if element.tag is not etree.Comment:
                if element.tag.split('}')[-1] == 'values':
                    has_values = True

                    if len(variable_shape) == 1:
                        length = dimensions[variable_shape[0]].size
                        start = float(element.attrib['start'])
                        step = float(element.attrib['incr'])
                        dimension_list = []

                        for number in range(length):
                            dimension_list.append(start)
                            start += step

                        variable_values = numpy.array(dimension_list)
                    else:
                        raise Exception
        return has_values, variable_values

    def parse_attribute_value(element, number_type):
        if validate_json(element.attrib['value']):
            if element.attrib['value'][0] == '[' and element.attrib['value'][-1] == ']':
                value_list = json.loads(element.attrib['value'])
                if number_type is not None:
                    value = numpy.array(value_list, dtype=number_type)
                else:
                    value = numpy.array(value_list)
            else:
                value = json.loads(element.attrib['value'])
                if number_type is not None and (isinstance(value, int) or isinstance(value, float)):
                    value = numpy.array(value, dtype=number_type)
        else:
            value = element.attrib['value']
        return value

    def get_attributes(xml_group):
        attribute_dictionary = {}

        for element in xml_group:
            if element.tag is not etree.Comment:
                if element.tag.split('}')[-1] == 'attribute':
                    value = parse_attribute_value(element, None)
                    attribute_dictionary[element.attrib['name']] = value

        return attribute_dictionary

    def add_attributes(xml_group, netcdf_element, number_type):
        attribute_dictionary = {}

        for element in xml_group:
            if element.tag is not etree.Comment:
                if element.tag.split('}')[-1] == 'attribute':
                    if element.attrib['name'] not in netcdf_element.ncattrs():
                        if element.attrib['name'] == 'units':
                            attribute_dictionary[element.attrib['name']] = str(element.attrib['value'])
                        else:
                            value = parse_attribute_value(element, number_type)
                            attribute_dictionary[element.attrib['name']] = value

        netcdf_element.setncatts(attribute_dictionary)
        return attribute_dictionary

    def iterate_group(xml_element, final_netcdf4_dataset_group, cfbuild_dataset_group, original_dataset_group):
        variable_dictionary = cfbuild_dataset_group.variables

        for element in xml_element:

            if element.tag is not etree.Comment:
                if element.tag.split('}')[-1] == 'dimension':
                    if element.attrib['length'] == 'None' or element.attrib['length'] == 'unlimited':
                        dimension_size = None
                    elif element.attrib['length'].isdigit():
                        dimension_size = int(element.attrib['length'])
                    else:
                        print('error')
                        dimension_size = None

                    if element.attrib['name'] not in final_netcdf4_dataset_group.dimensions:
                        final_netcdf4_dataset_group.createDimension(dimname=element.attrib['name'], size=dimension_size)

                elif element.tag.split('}')[-1] == 'variable':
                    has_values, element_values = check_element_for_values(element, eval(element.attrib['shape']),
                                                                          final_netcdf4_dataset_group.dimensions)

                    if 'orgName' in element.attrib:
                        original_name = element.attrib['orgName']
                        new_name = element.attrib['name']
                    else:
                        original_name = element.attrib['name']
                        new_name = element.attrib['name']

                    if has_values:
                        variable_values = element_values
                    elif variable_dictionary[original_name].values is None:
                        try:
                            variable_values = original_dataset_group.variables[original_name][:]
                        except Exception as e:
                            print(e)
                    else:
                        variable_values = variable_dictionary[original_name].values

                    if new_name in final_netcdf4_dataset_group.variables:
                        attributes = add_attributes(
                            element,
                            final_netcdf4_dataset_group.variables[new_name],
                            element.attrib['type']
                        )
                    else:
                        attributes = get_attributes(element)

                        if isinstance(variable_values, numpy.ndarray):
                            if '_FillValue' in attributes:
                                if isinstance(attributes['_FillValue'], str) or \
                                        isinstance(attributes['_FillValue'], bytes) or \
                                        isinstance(attributes['_FillValue'], bytearray):
                                    if validate_json(attributes['_FillValue']):
                                        fill_value = json.loads(attributes['_FillValue'])
                                    else:
                                        fill_value = attributes['_FillValue']
                                else:
                                    fill_value = attributes['_FillValue']
                            else:
                                if not numpy.ma.is_masked(variable_values):
                                    fill_value = variable_values.fill_value
                                else:
                                    fill_value = None

                            new_variable = final_netcdf4_dataset_group.createVariable(
                                varname=new_name,
                                datatype=element.attrib['type'],
                                dimensions=eval(element.attrib['shape']),
                                fill_value=fill_value
                            )

                            add_attributes(element, new_variable, element.attrib['type'])

                            if element.attrib['type'] != str(variable_values.dtype):
                                new_variable[:] = variable_values.astype(str(element.attrib['type']))
                            else:
                                new_variable[:] = variable_values

                elif element.tag.split('}')[-1] == 'group':
                    new_group = final_netcdf4_dataset_group.createGroup(groupname=element.attrib['name'])
                    iterate_group(element, new_group, original_dataset_group.groups[element.attrib['name']])

    tree = etree.parse(ncml_object.ncml_filepath)
    root = tree.getroot()
    cfbuild_dataset = ncml_object.dataset
    add_attributes(root, final_netcdf4_dataset, None)
    iterate_group(root, final_netcdf4_dataset, cfbuild_dataset, original_dataset)
