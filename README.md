# Elevate-Labs-Task-2
# Example: Survival by Age &amp; Sex if 'Survived' in df.columns and 'Age' in df.columns and 'Sex' in df.columns:     fig = px.histogram(df, x="Age", color="Sex", barmode="overlay", facet_col="Survived")     fig.update_layout(title="Age Distribution by Sex &amp; Survival")     fig.show()
