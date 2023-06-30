-- 17. Not my genre
-- List all genres not linked to the show Dexter
SELECT DISTINCT tv_g.name
FROM tv_genres tv_g
LEFT JOIN tv_show_genres tv_s_g
ON tv_g.id = tv_s_g.genre_id
LEFT JOIN tv_shows tv_s
ON tv_s.id = tv_s_g.show_id
WHERE tv_g.name NOT IN (SELECT tv_genres.name
FROM tv_show_genres 
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY tv_g.name ASC;
