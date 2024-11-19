# Set runtime config files
import pythonnet, clr_loader, os
bin_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),'bin','Debug','net9.0')
runtime_config_path = os.path.join(bin_folder,'pythonnet_minimal.runtimeconfig.json')
pythonnet.set_runtime(clr_loader.get_coreclr(runtime_config=runtime_config_path))

# Load library
import clr
dll_filepath = os.path.join(bin_folder,'pythonnet_minimal.dll')
clr.AddReference(dll_filepath)

# Register Encoder (optional)
import Python.Runtime
import api;
Python.Runtime.PyObjectConversions.RegisterEncoder(api.ColorsPythonEncoder.Instance);

# Using the C# library
a = api.Math.Sum(40,2);
color = api.Colors.Blue;
print("a: " +  str(a))
print("color: " + color) #Converted to string by the registered encoder

