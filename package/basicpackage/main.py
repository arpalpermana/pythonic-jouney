# basic usage of package/import
import package_data
from function.import_function import add

print(package_data.identity["name"])

print("".join([f"index {i} = {x} \n" for i, x in enumerate(package_data.number_data)]))

print(f"3 + 5 = {add(3,5)}")
