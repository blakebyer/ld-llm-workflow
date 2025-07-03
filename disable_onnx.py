import sys
import types
import importlib.machinery

# Create a fake ONNX module with a valid __spec__
onnx_fake = types.SimpleNamespace()
onnx_fake.__spec__ = importlib.machinery.ModuleSpec("onnxruntime", None)

# Insert into sys.modules before anything tries to import it
sys.modules["onnxruntime"] = onnx_fake