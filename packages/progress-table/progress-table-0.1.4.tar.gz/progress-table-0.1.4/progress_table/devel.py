import random
import time

from progress_table import ProgressTable

# Define the columns at the beginning
progress = ProgressTable(
    columns=["step", "x", "x squared"],

    # Default values:
    refresh_rate=10,
    num_decimal_places=4,
    default_column_width=8,
    print_row_on_update=True,
    reprint_header_every_n_rows=30,
    custom_format=None,
    embedded_progress_bar=False,
)
progress.add_column("x", width=3)
progress.add_column("x root", color="red")
progress.add_column("random average", color="bright", aggregate="mean")

for step in range(10):
    x = random.randint(0, 200)

    # There are two equivalent ways to add new values.

    # First:
    progress["step"] = step
    progress["x"] = x

    # Second:
    progress.update("x root", x ** 0.5)
    progress.update("x squared", x ** 2)

    # Display a progress bar by wrapping the iterator
    for _ in progress(range(10)):

        # You can use weights for aggregated values
        progress.update("random average", random.random(), weight=1)
        time.sleep(0.1)

    # Go to next row when you're ready
    progress.next_row()

# Close the table when it's ready
progress.close()

# Export your data
data = progress.to_list()
pandas_df = progress.to_df()
np_array = progress.to_numpy()
