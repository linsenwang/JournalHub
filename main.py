from flask import Flask, abort
import importlib

app = Flask(__name__)

@app.route('/<module_name>')
def dynamic_route(module_name):
    try:
        # 动态加载模块
        module = importlib.import_module(f'lib.routes.{module_name}')
        
        # 调用模块中的 handler 函数
        if hasattr(module, 'handler'):
            return module.handler()
        else:
            return abort(404, description=f"No 'handler' function in {module_name}")
    except ModuleNotFoundError:
        # 如果模块未找到
        return abort(404, description=f"Module '{module_name}' not found")

if __name__ == '__main__':
    app.run(debug=True)
