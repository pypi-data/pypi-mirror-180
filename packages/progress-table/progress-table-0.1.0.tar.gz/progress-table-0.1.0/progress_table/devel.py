import random
import time

from progress_table import ProgressTable

# At the beginning, define all the columns
progress = ProgressTable(columns=["step", "x"], num_decimal_places=6)
progress.add_column("x squared", aggregate="sum")
progress.add_column("x root", color="red", width=12)

for step in range(20):
    progress["step"] = step

    # Display a progress bar by wrapping the iterator
    for _ in progress(range(10)):
        time.sleep(0.1)

    x = random.randint(0, 200)

    # There are ways to add new values
    progress["x"] = x  # OR
    progress.update("x root", x ** 0.5)

    # You can use weights for aggregated values
    progress.update("x squared", x ** 2, weight=1)

    # Go to next row when you're ready
    progress.next_row()

# Close the table when it's ready
progress.close()

# Export your data
data = progress.to_list()
pandas_df = progress.to_df()
np_array = progress.to_numpy()
