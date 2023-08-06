from matplotlib import rcParams
import matplotlib.pyplot as plt
from cycler import cycler
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter
import pandas as pd
import matplotlib.lines as lines
import plotly.graph_objects as go
from plotly.graph_objs import Layout
from IPython.display import Image

def pareto(variable, title_show = False, salida='grafico'):
    #Ordenar en descendente y pasar a dataframe
    pareto = variable.sort_values(ascending=False).to_frame()
    #Cambiar el nombre a la variable
    pareto.columns = ['Valor']
    #Crear la posición
    pareto['Posicion'] = np.arange(start=1, stop=len(pareto) + 1)
    pareto['Posicion_Porc'] = pareto.Posicion.transform(
        lambda x: x / pareto.shape[0] * 100)
    #Crear el acumulado
    pareto['Acum'] = pareto['Valor'].cumsum()
    max_pareto_acum = max(pareto.Acum)
    pareto['Acum_Porc'] = pareto.Acum.transform(
        lambda x: x / max_pareto_acum * 100)
    #Simplificar
    pareto = pareto[['Posicion_Porc', 'Acum_Porc']]

    value = 80
    idx = (pareto["Acum_Porc"] - value).abs().idxmin()
    idx2 = pareto["Acum_Porc"].idxmin()
    nearest = pareto["Posicion_Porc"].loc[idx]
    ini = pareto["Posicion_Porc"].loc[idx2]

    #Devolver la salida
    if salida == 'grafico':
        f, ax = plt.subplots(figsize=(11, 7),dpi=85)
        ax.plot(pareto.Posicion_Porc, pareto.Acum_Porc,color='#97ACCF')
        ax.plot(pareto.Posicion_Porc, pareto.Posicion_Porc,color="#364D6E")
        ax.tick_params(axis='x', labelsize=12, labelrotation=90)
        ax.set_xticks(pareto.Posicion_Porc, pareto.index, rotation='vertical')
        ax.axvline(nearest, color="#D6D7D9", alpha=0.3)
        ax.text(nearest + 2, 0, "%.1f %%" % (nearest))
        ax.axhline(80, color="#D6D7D9", alpha=0.3, linestyle='dotted')
        if title_show:
            ax.set_title("Pareto graph for '%s' by '%s'" %
                         (variable.name, variable.index.name))
        ax.fill_between([ini, nearest, nearest, ini], [0, 0, 100, 100],
                        alpha=0.3,
                        color="#D6D7D9")
        return (ax)
    else:
        return (pareto)
        
def histogram(df,value,labelx=None,labely=None,figsize=(11,7),dpi=85):
    f = plt.figure(figsize=figsize,dpi=dpi)
    ax = sns.histplot(df,x=value,shrink=0.8)
    xlocs, xlabs = plt.xticks()
    j = 0
    for i,v in zip(df[value].value_counts(sort=False).index,df[value].value_counts(sort=False)):
        plt.text(xlocs[j], v+2, int(v), ha='center', fontsize=12)
        j+=1

    if labelx is not None:
        plt.xlabel(labelx, c="#364D6E", fontsize=14)
    if labely is not None:
        plt.ylabel(labely, c="#364D6E", fontsize=14)
    # remove y ticks
    plt.yticks([])
    return f, ax

def histmax(df,value,labelx=None,labely=None,
                   max_color="#364D6E",other_color="#D6D7D9",
                   figsize=(11,7),dpi=85):

    series = df[value].value_counts(sort=False)
    max_val = df[value].value_counts(sort=False).max()
    pal = []

    for item in series:
        if item == max_val:
            pal.append(max_color)
        else:
            pal.append(other_color)

    f = plt.figure(figsize=figsize,dpi=dpi)
    ax = sns.barplot(x = df[value].value_counts(sort=False).index,
                     y = df[value].value_counts(sort=False),
                palette=pal)

    xlocs, xlabs = plt.xticks()
    j = 0
    for i,v in zip(df[value].value_counts(sort=False).index,
                   df[value].value_counts(sort=False)):
        plt.text(xlocs[j], v+2, int(v), ha='center', fontsize=12)
        j+=1

    if labelx is not None:
        plt.xlabel(labelx, c="#364D6E", fontsize=14)
    if labely is not None:
        plt.ylabel(labely, c="#364D6E", fontsize=14)
    # remove y ticks
    plt.yticks([])
    return f, ax

def waterfall(df,valor,group=False,group_value="",
                     Title="", x_lab="", y_lab="",
                     formatting = "{:,.1f}",
                     unidad = "",
                     green_color="#D6D7D9", 
                     red_color="#D6D7D9", 
                     blue_color="#364D6E",
                     sorted_value = False, 
                     threshold=None, 
                     other_label='other', 
                     net_label='net', 
                     rotation_value = 30, 
                     blank_color=(0,0,0,0), 
                     figsize = (9,6),
                     dpi = 85):
    if group == True:
        df = df.groupby(group_value)[valor].sum().reset_index().set_index(group_value)
    index = df.index
    data = df[valor].values
    '''
    Given two sequences ordered appropriately, generate a standard waterfall chart.
    Optionally modify the title, axis labels, number formatting, bar colors, 
    increment sorting, and thresholding. Thresholding groups lower magnitude changes
    into a combined group to display as a single entity on the chart.
    '''
    
    #convert data and index to np.array
    index=np.array(index)
    data=np.array(data)
    
    # wip
    #sorted by absolute value 
    if sorted_value: 
        abs_data = abs(data)
        data_order = np.argsort(abs_data)[::-1]
        data = data[data_order]
        index = index[data_order]
    
    #group contributors less than the threshold into 'other' 
    if threshold:
        
        abs_data = abs(data)
        threshold_v = abs_data.max()*threshold
        
        if threshold_v > abs_data.min():
            index = np.append(index[abs_data>=threshold_v],other_label)
            data = np.append(data[abs_data>=threshold_v],sum(data[abs_data<threshold_v]))
    
    changes = {'amount' : data}
    
    #define format formatter
    def money(x, pos):
        'The two args are the value and tick position'
        return formatting.format(x)
    formatter = FuncFormatter(money)
    
    fig, ax = plt.subplots(figsize=figsize,dpi=dpi)
    ax.yaxis.set_major_formatter(formatter)

    #Store data and create a blank series to use for the waterfall
    trans = pd.DataFrame(data=changes,index=index)
    blank = trans.amount.cumsum().shift(1).fillna(0)
    
    trans['positive'] = trans['amount'] > 0

    #Get the net total number for the final element in the waterfall
    total = trans.sum().amount
    trans.loc[net_label]= total
    blank.loc[net_label] = total

    #The steps graphically show the levels as well as used for label placement
    step = blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan

    #When plotting the last element, we want to show the full bar,
    #Set the blank to 0
    blank.loc[net_label] = 0
    
    #define bar colors for net bar
    trans.loc[trans['positive'] > 1, 'positive'] = 99
    trans.loc[trans['positive'] < 0, 'positive'] = 99
    trans.loc[(trans['positive'] > 0) & (trans['positive'] < 1), 'positive'] = 99
    
    trans['color'] = trans['positive']
    
    trans.loc[trans['positive'] == 1, 'color'] = green_color
    trans.loc[trans['positive'] == 0, 'color'] = red_color
    trans.loc[trans['positive'] == 99, 'color'] = blue_color
    
    my_colors = list(trans.color)
    
    #Plot and label
    my_plot = plt.bar(range(0,len(trans.index)), blank, width=0.5, color=blank_color)
    plt.bar(range(0,len(trans.index)), trans.amount, width=0.6,
             bottom=blank, color=my_colors)       
                                   
    
    plt.plot(step.index, step.values,alpha=0.4,ls=':')
    
    #axis labels
    plt.xlabel("\n" + x_lab)
    plt.ylabel(y_lab + "\n")

    #Get the y-axis position for the labels
    y_height = trans.amount.cumsum().shift(1).fillna(0)
    
    temp = list(trans.amount)
    
    # create dynamic chart range
    for i in range(len(temp)):
        if (i > 0) & (i < (len(temp) - 1)):
            temp[i] = temp[i] + temp[i-1]
    
    trans['temp'] = temp
            
    plot_max = trans['temp'].max()
    plot_min = trans['temp'].min()
    
    #Make sure the plot doesn't accidentally focus only on the changes in the data
    if all(i >= 0 for i in temp):
        plot_min = 0
    if all(i < 0 for i in temp):
        plot_max = 0
    
    if abs(plot_max) >= abs(plot_min):
        maxmax = abs(plot_max)   
    else:
        maxmax = abs(plot_min)
        
    pos_offset = maxmax / 150
    
    plot_offset = maxmax / 30 ## needs to me cumulative sum dynamic

    #Start label loop
    loop = 0
    for index, row in trans.iterrows():
        # For the last item in the list, we don't want to double count
        if row['amount'] == total:
            y = y_height[loop]
        else:
            y = y_height[loop] + row['amount']
        # Determine if we want a neg or pos offset
        if row['amount'] > 0:
            y += (pos_offset*2)
            plt.annotate(formatting.format(row['amount'])+"%s"%(unidad),(loop,y),ha="center", fontsize=10)
        else:
            y -= (pos_offset*4)
            plt.annotate(formatting.format(row['amount'])+"%s"%(unidad),(loop,y),ha="center", fontsize=10)
        loop+=1

    #Scale up the y axis so there is room for the labels
    plt.ylim(plot_min-round(3.6*plot_offset, 7),plot_max+round(3.6*plot_offset, 7))
    
    #Rotate the labels
    plt.xticks(range(0,len(trans)), trans.index, rotation=rotation_value)
    
    #add zero line and title
    plt.axhline(0, color='black', linewidth = 0.6, linestyle="dashed")
    # remove y ticks
    plt.yticks([])
    plt.title(Title)
    plt.tight_layout()

    return fig, ax

def lollipop(df,valor1,valor2,unidad="",figsize=(11,7),dpi=85,linewidth=5,size=10,textsize=12,offset=9,color='grey'):
    f, ax = plt.subplots(figsize=figsize,dpi=dpi)
    markers,stems,base = plt.stem(df[valor1],df[valor2])
    plt.setp(stems, 'linewidth', linewidth)
    markers.set_markersize(size)
    markers.set_color(color)
    xlocs, xlabs = plt.xticks()
    j = 0
    for v in df[valor2]:
        plt.text(xlocs[j], v+offset, "%.2f %s"%(v,unidad), ha='center', fontsize=textsize)
        j+=1
    plt.ylabel("")
    plt.yticks([])                                    
    return f, ax

def mekko(ynp_values,xnp_values,x_label,figsize=(12,7),color1='#97ACCF',color2='#D6D7D9',xticks_size=14,legend1='val1',legend2='val2',title_size=20,legend_size=20,label_y="",label_x="",title=""):
    # calculate x coordinates based on the width of the previous bars
    # same as: [0, width[0], width[0] + width[1], width[0] + width[1] + width[2]]
    y = ynp_values
    x = xnp_values
    width = [i/sum(x) for i in x]
    f, ax = plt.subplots(figsize=figsize)
    rcParams['axes.titley'] = 1.25
    adjusted_x, temp = [0], 0
    for i in width[:-1]:
        temp += i
        adjusted_x.append(temp)
    # Marimekko chart
    plt.bar(adjusted_x, y, width=width, align='edge', edgecolor='black',color=color1,alpha=0.7)
    plt.bar(adjusted_x, np.ones(len(y))-y, bottom=y, width=width, align='edge', edgecolor='black',color=color2,alpha=0.7)
    # x and y ticks (%)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
    plt.ylim(0,1)
    plt.xlim(0,1)
    # twin y-axis to draw x-ticks at the top
    axy = ax.twiny()
    axy.set_xticks([(width[i]/2)+ v for i, v in enumerate(adjusted_x)])
    axy.set_xticklabels(x_label, fontsize=xticks_size)
    ax.set_ylabel(label_y)
    ax.set_xlabel(label_x)
    ax.spines.right.set_visible(True)
    plt.title(title,
              loc='left', fontsize=title_size)
    ax.legend([legend1,legend2], 
               ncol=2, loc='upper left', fontsize=legend_size,
                   frameon=False, bbox_to_anchor=(0,1.25))
    return f, ax

def sankey(source, target, value,labels_sr,labels_tr,label_show=False, opacity_ins=0.5):
    """
    Gráfico tipo Sankey
    """
    opacity = str(opacity_ins)
    color_rgb = []
    color_rgb.append('rgba(151, 172, 207, %s)'%(opacity))
    color_rgb.append('rgba(110, 127, 128, %s)'%(opacity))
    color_rgb.append('rgba(0, 105, 148, %s)'%(opacity))
    color_rgb.append('rgba(83, 104, 114, %s)'%(opacity))
    color_rgb.append('rgba(201, 239, 254, %s)'%(opacity))
    color_rgb.append('rgba(54, 69, 79, %s)'%(opacity))
    color_rgb.append('rgba(178, 203, 245, %s)'%(opacity))
    color_rgb.append('rgba(42, 192, 251, %s)'%(opacity))
    color_rgb.append('rgba(137, 207, 240, %s)'%(opacity))
    color_rgb.append('rgba(95, 108, 130, %s)'%(opacity))
    
    if label_show:
        color_label='black'
    else:
        color_label="rgba(0,0,0,0)"

    config = {
      'displayModeBar': False,
    }
    
    color_node = []
    
    for i in range(0,len(labels_sr)):
        color_node.append(color_rgb[i])
        
    for i in range(0,len(labels_sr)):
        color_node.append('white')

    labels=labels_sr + labels_tr
    
    color_link = []
    # link color
    for i in source:
        color_link.append(color_rgb[i])

    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 20,
          thickness = 1,
          line = dict(color = "black", width = 0),
          label = labels,
          color = color_node
        ),
        textfont=dict(color=color_label, size=12),
        link = dict(
          source = source, # indices correspond to labels, eg A1, A2, A1, B1, ...
          target = target,
          value = value,
          color = color_link
      ))])
    img_bytes = fig.to_image(format="png",height=600,width=800)
    return Image(img_bytes)
    
def funnel(labels, values, opacity_ins=0.5):
    opacity = str(opacity_ins)
    color_rgb = []
    color_rgb.append('rgba(151, 172, 207, %s)'%(opacity))
    color_rgb.append('rgba(110, 127, 128, %s)'%(opacity))
    color_rgb.append('rgba(0, 105, 148, %s)'%(opacity))
    color_rgb.append('rgba(83, 104, 114, %s)'%(opacity))
    color_rgb.append('rgba(201, 239, 254, %s)'%(opacity))
    color_rgb.append('rgba(54, 69, 79, %s)'%(opacity))
    color_rgb.append('rgba(178, 203, 245, %s)'%(opacity))
    color_rgb.append('rgba(42, 192, 251, %s)'%(opacity))
    color_rgb.append('rgba(137, 207, 240, %s)'%(opacity))
    color_rgb.append('rgba(95, 108, 130, %s)'%(opacity))

    config = {
      'displayModeBar': False,
    }
    
    color_node = []
    
    for i in range(0,len(labels)):
        color_node.append(color_rgb[i])
        
    layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(go.Funnel(
                    y = labels,
                    x = values,
                    textposition = "inside",
                    textinfo = "value+percent initial",
                    opacity=opacity_ins,
                    marker = {"color": color_node,}
                            ),
    layout=layout)
    

    
    img_bytes = fig.to_image(format="png",height=600,width=800)
    return Image(img_bytes)