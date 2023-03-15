-- List all Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
AND tv_genres.name = 'Comedy'
ORDER BY title;
