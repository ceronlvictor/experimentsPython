from bokeh.plotting import figure, output_file, show     #figure(Es la ventrana donde vamos a graficar), output_file(Determinar el nombre del archivo),

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores queires graficar? '))
    x_vals = list(range(total_vals))
    y_vals = []
    
    for x in x_vals:
        val = int(input(f'Valor y para {x}  '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)

