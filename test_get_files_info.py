from functions.get_files_info import get_files_info

print (f"Result for current directory")
result = get_files_info("calculator", ".")
print(result)

print (f"Result for pkg directory")
pkg_result = get_files_info("calculator", "pkg")
print(pkg_result)

print (f"Result for /bin directory")
bin_result = get_files_info("calculator", "/bin")
print(bin_result)

print (f"Result for parent directory")
dot_result = get_files_info("calculator", "../")
print (dot_result)