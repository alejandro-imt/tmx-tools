# Program to generate beautiful graphs and plots with dash and plotly
# @organization: Tecnología México (TMx)
# @author: Alejandro Peñuelas
# @date: 09/02/2025
# @version: 1.0
import numpy as np
import plotly.graph_objs as go
from generate_plotly_templates import light_template

# Generate the light template
tmx_light_template = light_template()

# Function to generate synthetic data
def generate_data(length: int=50, num_signals: int=1, type: str='random', sin_components: int=10, max_amplitude: float=1, 
                  offset: float=0) -> list[np.array]:
    # Initialize data
    data = [np.zeros(length) for _ in range(num_signals)]
    
    # Random data
    if type == 'random':
        for sig in range(num_signals):
            data[sig] = np.random.rand(length) * max_amplitude + offset

    # Sinusoidal data
    elif type == 'sinusoidal':
        for sig in range(num_signals):    
            # Define [sin_components] random sinusoidal components and sum them
            signal = np.zeros(length)
            for _ in range(sin_components):
                amplitude = np.random.rand() * (max_amplitude / sin_components)
                frequency = np.random.rand() * 10
                phase = np.random.rand() * 2*np.pi
                signal += amplitude * np.sin(np.linspace(0, 2*np.pi, length) * frequency + phase)
            data[sig] = signal + offset
    
    # Square wave data
    elif type == 'squared':
        for sig in range(num_signals):
            data[sig] = (np.random.randint(0, 2, length)) * max_amplitude + offset
    return data

# Function to generate a plot with lines and dots
def plot_lines_and_dots(data: list[np.array]=None, title: str='Plot lines', 
                        x_label: str='X label', y_label: str='Y label') -> go.Figure:
    fig = go.Figure()
    
    # Add traces per element in data
    for i, data_vector in enumerate(data):
        trace = go.Scatter(x=np.arange(len(data_vector)), y=data_vector, mode='lines+markers', name=f'Data {i}')
        fig.add_trace(trace)
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return fig


# Function to generate a plot with only lines
def plot_lines(data_list: list[np.array]=None, title: str = "Plot lines",
               x_label: str = "X label", y_label: str = "Y label") -> go.Figure:
    # Create a figure
    fig = go.Figure()
    
    # Add traces per element in data
    for i, data_vector in enumerate(data_list):
        trace = go.Line(x=np.arange(len(data_vector)), y=data_vector, mode='lines', name=f'Data {i}')
        fig.add_trace(trace)
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return fig

# Function to generate bar plots
def plot_bars(data_list: list[np.array]=None, title: str = "Bar plot",
              x_label: str = "X label", y_label: str = "Y label") -> go.Figure:
        # Create a figure
        fig = go.Figure()
        
        # Add traces per element in data
        for i, data_vector in enumerate(data_list):
            trace = go.Bar(x=np.arange(len(data_vector)), y=data_vector, name=f'Data {i}')
            fig.add_trace(trace)
        fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
        return fig

# Function to generate buble plots
def plot_bubbles(data_list: list[np.array]=None, bubble_size: list[int]=None, title: str = "Bubble plot",
                 x_label: str = "X label", y_label: str = "Y label") -> go.Figure:
    # Create a figure
    fig = go.Figure()
    
    # Add traces per element in data
    for i, data_vector in enumerate(data_list):
        trace = go.Scatter(
            x=np.arange(len(data_vector)), y=data_vector, mode='markers', marker_symbol='circle', name=f'Data {i}',
            marker_size=bubble_size[i]
            )
        fig.add_trace(trace)
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return fig

if __name__ == '__main__':

    # Generate synthetic data as sinusoidal signals
    data = generate_data(length=100, num_signals=3, type='sinusoidal', max_amplitude=10, offset=30)

    # Generate synthetic data as random signals
    # data = generate_data(length=100, num_signals=1, type='random', max_amplitude=10, offset=30)

    # Generate synthetic data as squared signals
    # data = generate_data(length=100, num_signals=1, type='squared')

    # Scatter plot with lines and dots
    fig = plot_lines_and_dots(data, title='Sinusoidal Plot', x_label='Time', y_label='Amplitude')

    # Line plot
    # fig = plot_lines(data, title='Sinusoidal Plot', x_label='Time', y_label='Position')
    
    # Bar plot
    # fig = plot_bars(data, title='Bar plot', x_label='Time', y_label='Amplitude')
    
    # Bubble plot
    # bubble_size = [[np.random.randint(1, 100) for _ in range(len(data[0]))] for _ in range(len(data))]  
    # fig = plot_bubbles(data, bubble_size=bubble_size, title='Bubble plot', x_label='Time', y_label='Position')

    # Update the layout with the TMX template
    fig.update_layout(template=tmx_light_template)
    
    # Show the plot
    fig.show()
