from functions.get_file_content import get_file_content

print (f"Result for lorem.txt")
result = get_file_content("calculator", "lorem.txt")
print (len(result))

print (f"Result for main.py")
main_result = get_file_content("calculator", "main.py")
print(main_result)

print (f"Result for pkg/calculator.py")
pkg_result = get_file_content("calculator", "pkg/calculator.py")
print(pkg_result)

print (f"Result for bin/cat")
bin_result = get_file_content("calculator", "/bin/cat")
print (bin_result)

print (f"Result for no_pkg")
no_pkg_result = get_file_content("calculator", "pkg/does_not_exist.py")
print (no_pkg_result)