# Finds content providers/resolvers on Android devices 

### Some things you have to know:

- You might need root access 
- I have only tested it against BlueStacks / Windows 10 / Python 3.9.


```python

$pip install fetch-content-providers-and-resolvers


from fetch_content_providers_and_resolvers import ContentProviderResolverFetcher
adb_path = "C:\\Users\\Gamer\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe"
deviceserial = "localhost:5875"
cpr = ContentProviderResolverFetcher(
    adb_path=adb_path,
    deviceserial=deviceserial,
    folder="data/",  # As far as I know, this folder exists on any Android device, so you don't have to change anything
    folder_for_temp_files=r"F:\ctestprov",  # Folder to store the temp dex files
    ripgrep_path="rg.exe",  # Download RipGrep https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-pc-windows-gnu.zip
)
cpr.connect_to_adb()
cpr.get_all_files()  # Find all dex files / If you want to limit the packages to scan, you can modify cpr.df
cpr.pull_files()  # Copy the files to the hard drive
cpr.extract_content_providers()
cpr.check_results(
    exit_keys="ctrl+x", print_output=True, timeout=None,
)  # If you press ctrl+x you can kill a query which got stuck, you can also set a timeout for each query
df = cpr.get_all_results_checked()  # returns checked results
df1 = cpr.get_all_results()  # returns unchecked results



```
