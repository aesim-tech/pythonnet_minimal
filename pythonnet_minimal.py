# Set runtime config files
import pythonnet, os, sys
bin_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),'bin','Debug','net9.0')
if bin_folder not in sys.path:
    sys.path.insert(0, bin_folder)

runtime_config_path = os.path.join(bin_folder,'pythonnet_minimal.runtimeconfig.json')
pythonnet.load(runtime="coreclr",runtime_config=runtime_config_path)

import clr
clr.AddReference("pythonnet_minimal")

# Register Encoder (optional)
import Python.Runtime
import api;
Python.Runtime.PyObjectConversions.RegisterEncoder(api.ColorsPythonEncoder.Instance);

# Using the C# library
a = api.Math.Sum(40,2);
color = api.Colors.Blue;
print("a: " +  str(a))
print("color: " + color) #Converted to string by the registered encoder

