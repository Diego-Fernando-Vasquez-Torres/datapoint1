from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def landing():
    # Datos simulados que se pasarán al template (pueden ser reemplazados por datos reales de una base de datos)
    datos_insights = {
        'total_ingresos': 25000,
        'productos_vendidos': 3200,
        'categoria_mas_vendida': 'Electrónicos',
        'producto_mas_vendido': 'Auriculares Bluetooth'
    }
    
    ventas_recientes = [
        {'fecha': '01/11/2024', 'producto': 'Auriculares Bluetooth', 'cantidad': 5, 'total': 250},
        {'fecha': '03/11/2024', 'producto': 'Teclado Mecánico', 'cantidad': 2, 'total': 140},
        {'fecha': '05/11/2024', 'producto': 'Smartwatch', 'cantidad': 1, 'total': 120}
    ]

    # Pasamos 'inicio' como la página activa
    return render_template('landing.html', datos_insights=datos_insights, ventas_recientes=ventas_recientes, active_page='inicio')

@app.route('/ventas')
def ventas():
    # Pasamos 'ventas' como la página activa
    return render_template('ventas.html', active_page='ventas')

@app.route('/compras')
def compras():
    # Pasamos 'compras' como la página activa
    return render_template('compras.html', active_page='compras')

@app.route('/configuracion')
def configuracion():
    # Pasamos 'configuracion' como la página activa
    return render_template('configuracion.html', active_page='configuracion')

@app.route('/formalizar')
def formalizar():
    # Pasamos 'formalizacion' como la página activa
    return render_template('formalizar.html', active_page='formalizacion')

if __name__ == '__main__':
    app.run(debug=True)
