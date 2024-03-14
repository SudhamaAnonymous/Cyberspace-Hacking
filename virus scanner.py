from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'



# create an instance of the API class
api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
input_file = '/path/to/inputfile' # file | Input file to perform the operation on.
allow_executables = True # bool | Set to false to block executable files (program code) from being allowed in the input file.  Default is false (recommended). (optional)
allow_invalid_files = true # bool | Set to false to block invalid files, such as a PDF file that is not really a valid PDF file, or a Word Document that is not a valid Word Document.  Default is false (recommended). (optional)
allow_scripts = true # bool | Set to false to block script files, such as a PHP files, Python scripts, and other malicious content or security threats that can be embedded in the file.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_password_protected_files = true # bool | Set to false to block password protected and encrypted files, such as encrypted zip and rar files, and other files that seek to circumvent scanning through passwords.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_macros = true # bool | Set to false to block macros and other threats embedded in document files, such as Word, Excel and PowerPoint embedded Macros, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_xml_external_entities = true # bool | Set to false to block XML External Entities and other threats embedded in XML files, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_insecure_deserialization = true # bool | Set to false to block Insecure Deserialization and other threats embedded in JSON and other object serialization files, and other files that contain embedded content threats.  Set to true to allow these file types.  Default is false (recommended). (optional)
allow_html = true # bool | Set to false to block HTML input in the top level file; HTML can contain XSS, scripts, local file accesses and other threats.  Set to true to allow these file types.  Default is false (recommended) [for API keys created prior to the release of this feature default is true for backward compatability]. (optional)
restrict_file_types = 'restrict_file_types_example' # str | Specify a restricted set of file formats to allow as clean as a comma-separated list of file formats, such as .pdf,.docx,.png would allow only PDF, PNG and Word document files.  All files must pass content verification against this list of file formats, if they do not, then the result will be returned as CleanResult=false.  Set restrictFileTypes parameter to null or empty string to disable; default is disabled. (optional)

try:
    # Advanced Scan a file for viruses
    api_response = api_instance.scan_file_advanced(input_file, allow_executables=allow_executables, allow_invalid_files=allow_invalid_files, allow_scripts=allow_scripts, allow_password_protected_files=allow_password_protected_files, allow_macros=allow_macros, allow_xml_external_entities=allow_xml_external_entities, allow_insecure_deserialization=allow_insecure_deserialization, allow_html=allow_html, restrict_file_types=restrict_file_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scan_file_advanced: %s\n" % e)