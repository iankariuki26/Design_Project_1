from database_manager import MovieLensDB

def check_results():
    db = MovieLensDB()
    
    query = """
    SELECT title, round(avg_rating, 2) as rating, review_count 
    FROM filtered_movies 
    ORDER BY avg_rating DESC 
    LIMIT 5;
    """
    
    result = db.execute_query(query).df()
    print("\n--- PIPELINE CHECK: TOP 5 HIDDEN GEMS ---")
    print(result)
    
    db.close()

if __name__ == "__main__":
    check_results()