import ast
# import builtins

def run(source_file, params):
    # Read the source file
    with open(source_file, 'r') as file:
        source_code = file.read()

    parsed_code = ast.parse(source_code, filename=source_file)
    compiled_code = compile(parsed_code, filename=source_file, mode='exec')

    namespace = params
    # namespace['__builtins__'] = builtins
    exec(compiled_code, namespace)

    output = namespace.get('output')
    return output
    

if __name__ == '__main__':
    # print(run('doit.py', {"num_rows": 500, "num_cols": 20}))
    print( run('x1.py', {"a": 5, "b": 0}) )