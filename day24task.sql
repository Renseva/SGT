select substring(InvoiceDate, 1, 4), sum(total) from invoices i 
group by substring(InvoiceDate, 1, 4);

select country, sum(total) as Total_sales from invoices i 
join customers c 
on i.CustomerId = c.CustomerId
group by country;

select name, count(trackid) as Playlist_tracks from playlists p 
full join playlist_track pt 
on p.PlaylistId = pt.PlaylistId 
group by Name;