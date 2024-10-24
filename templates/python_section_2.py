import pandas as pd

def calculate_distance_matrix(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Create a distance matrix with IDs as both rows and columns
    ids = df['id_start'].unique()
    distance_matrix = pd.DataFrame(0, index=ids, columns=ids)

    for _, row in df.iterrows():
        start, end, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start, end] = distance
        distance_matrix.at[end, start] = distance  # Make it symmetric

    # Cumulative distances
    for k in ids:
        for i in ids:
            for j in ids:
                distance_matrix.at[i, j] = min(distance_matrix.at[i, j], 
                                                 distance_matrix.at[i, k] + distance_matrix.at[k, j])
    
    return distance_matrix


def unroll_distance_matrix(distance_matrix):
    unrolled_df = distance_matrix.stack().reset_index()
    unrolled_df.columns = ['id_start', 'id_end', 'distance']
    # Remove rows where id_start is the same as id_end
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]
    return unrolled_df

def calculate_toll_rate(unrolled_df):
    toll_rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle, rate in toll_rates.items():
        unrolled_df[vehicle] = unrolled_df['distance'] * rate
        
    return unrolled_df

