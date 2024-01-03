import yaml
import sys

def merge_yaml_files(file1, file2, output_file):

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # data1 = yaml.safe_load(f1)
        # data2 = yaml.safe_load(f2)
        data1 = yaml.load(f1, Loader=yaml.Loader)
        data2 = yaml.load(f2, Loader=yaml.Loader)
        merged_data = merge_dicts(data1, data2)

    with open(output_file, 'w') as out_file:
        yaml.dump(merged_data, out_file, default_flow_style=False)

def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            dict1[key] = merge_dicts(dict1[key], value)
        else:
            dict1[key] = value
    return dict1
    
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python combine_mkdocs_config_yaml.py <common_mkdocs_file_path> <override_mkdocs_file_path> <output_path>")
        sys.exit(1)
    common_mkdocs_file_path = sys.argv[1]
    override_mkdocs_file_path = sys.argv[2]
    output_path = sys.argv[3]

    merge_yaml_files(common_mkdocs_file_path, override_mkdocs_file_path, output_path)
    print(f"YAML files merged successfully. Merged file saved at {output_path}")
