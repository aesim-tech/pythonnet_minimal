using Python.Runtime;

namespace api
{
    public enum Colors { Blue, Red, Green }

    public static class Math
    {
        public static int Sum(int a, int b)
        {
            return a + b;
        }
    }

    public class ColorsPythonEncoder : IPyObjectEncoder
    {
        public static ColorsPythonEncoder Instance { get; } = new ColorsPythonEncoder();

        public bool CanEncode(Type type)
        {
            return type == typeof(Colors);
        }

        public PyObject? TryEncode(object value)
        {
            if (value == null) return null;

            if (value is Colors color)
            {
                string? name = Enum.GetName(typeof(Colors), color);
                if (name == null) return null;
                return new PyString(name);
            }
            return null;
        }

        public static void Register()
        {
            PyObjectConversions.RegisterEncoder(Instance);
        }
    }

}

