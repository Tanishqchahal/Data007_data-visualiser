import pandas as pd
import matplotlib.pyplot as plt


code = None

def execute_code(code: str, df: pd.DataFrame):
    # Create a namespace dictionary to safely execute the code
    namespace = {"df" : df}

    try:
        # Execute the code within the provided namespace
        res = eval(code, globals(), namespace)

        print(namespace)

        if isinstance(res, pd.DataFrame):
                return res

        if isinstance(res, plt.Axes):
                return res.get_figure()
        
        if isinstance(res, plt.Figure):
                return res
        
        if isinstance(res, str):
                return res
        
        if isinstance(res, int):
                return f"{res}"
        
        if isinstance(res, float):
                return f"{res}"
        
        if isinstance(res, list):
                return f'{res}'
        
        if isinstance(res, dict):
                return f'{res}'
        
        if isinstance(res, tuple):
                return f'{res}'
        
    except(SyntaxError, NameError):
         exec(code, globals(), namespace)

    # Check if a figure was created
    fig = plt.gcf()
    if fig.get_axes():
        return fig
    
    # Check for DataFrame objects in the namespace
    dataframes = [value for value in namespace.values() if isinstance(value, pd.DataFrame) and id(value) != id(df)]
    if dataframes:
        return dataframes[0]  # Return the first DataFrame found

    return None
       


