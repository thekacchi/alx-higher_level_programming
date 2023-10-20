-- List list all genres not linked to the show Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE (tv_shows.title != 'Dexter' OR tv_shows.title IS NULL)
  AND tv_genres.id NOT IN (
    SELECT tv_genres.id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
  )
ORDER BY tv_genres.name;
