import plotly.graph_objects as go


def get_input():
    sequence = input("I/O sequence (separated by space): ").split()
    sequence = [int(i) for i in sequence]
    return sequence



def display_chart(y):
    x = [i for i in range(len(y)+1)]
    
    fig = go.Figure()

    # Scatter Plot with Labels
    scatter = go.Scatter(
        x=x,
        y=y,
        mode='lines+markers+text',  # Include both markers and text
        text=y,  # Assign labels to the text attribute
        textposition='top center',  # Position of the labels relative to the points
        marker=dict(size=10),
        name='Scatter Plot'
    )

    fig.add_trace(scatter)

    # Customize Layout (Optional)
    fig.update_layout(
        title='Disk Scheduling with FCFS',
        xaxis_title=' ',
        yaxis_title='Track Number',
        xaxis=dict(range=[0, len(y)]),
        yaxis=dict(range=[0, 199])
    )

    fig.show()

# --------------------------------

seq = get_input()

# add the inital head
inithead = 50
seq.insert(0, inithead)

display_chart(seq)


# 176 79 34 60 92 11 41 114