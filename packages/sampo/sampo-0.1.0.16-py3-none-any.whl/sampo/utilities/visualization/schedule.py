from datetime import timedelta
from typing import Optional

import pandas as pd
import plotly.express as px

from sampo.utilities.visualization.base import VisualizationMode, visualize


def schedule_gant_chart_fig(schedule_dataframe: pd.DataFrame,
                            visualization: VisualizationMode,
                            fig_file_name: Optional[str] = None):
    """
    Creates and saves a gant chart of the scheduled tasks to the specified path.
    :param fig_file_name:
    :param visualization:
    :param schedule_dataframe: Pandas DataFrame with the information about schedule
    """
    print(schedule_dataframe.start.dtype)
    fig = px.timeline(schedule_dataframe, x_start='start', x_end='finish', y='idx', hover_name='task_name',
                      color=schedule_dataframe.loc[:, 'contractor'],
                      hover_data=['workers', 'contractor'],
                      title=f"{'Project tasks - Gant chart'}",
                      category_orders={'idx': list(schedule_dataframe.idx)},
                      text='task_name')
    fig.update_traces(textposition='outside')
    fig.update_yaxes(showticklabels=False, title_text='Project tasks',
                     range=[schedule_dataframe.loc[:, 'idx'].min(), schedule_dataframe.loc[:, 'idx'].max()])
    fig.update_xaxes(range=[schedule_dataframe.loc[:, 'start'].dt.min() - timedelta(days=2),
                            schedule_dataframe.loc[:, 'finish'].dt.max() + timedelta(days=25)],
                     title_text='Date')
    fig.update_layout(autosize=True, margin_autoexpand=True, font_size=12)

    return visualize(fig, mode=visualization, file_name=fig_file_name)
