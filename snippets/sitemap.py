def sitemap():
	import datetime
	import urllib
	siteMap = '<?xml version="1.0" encoding="UTF-8"?>\n'
	siteMap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
	siteMap +=  '<url>\n<loc>http://shoesonloose.com/</loc>\n<lastmod>2005-01-01</lastmod>\n<changefreq>monthly</changefreq>\n<priority>1.0</priority>\n</url>\n'
	x = db((db.Main_Table.id >0)).select()
	for row in x:
		title = row.location.replace(", ","_").replace(" ","-")
		url = URL('default','location',args=[title],host=True, extension=False)
		date = row.modified_on.strftime('%Y-%m-%d')
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.8</priority>\n</url>\n' %(url,date)
	x= db((db.blog.id>0)).select()
	for row in x:
		link = row.link.split()[0] if row.link != '' and row.link!=None else row.id
		url = URL('blog', 'blogs', args=[link], extension=False, host=True)
		date = row.modified_on.strftime('%Y-%m-%d')
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.7</priority>\n</url>\n' %(url,date)
	x = db((db.Trip.id>0) & (db.Trip.parent_trip==None)).select()
	for row in x:
		title =  "%s-%s" %(str(row.id),row.Trip_name)
		url = URL('default','trip',args=[title],extension=False,host=True)
		date = row.modified_on.strftime('%Y-%m-%d')
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n' %(url,date)
	x = ['adventure', 'culture','historical','sightseeing','wildlife']
	for row in x:
		url = URL('default','tag',args=[row],extension=False, host=True)
		date = '2015-07-08'
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n' %(url,date)
	x = db((db.Tag_Table.tag_id == db.Tag.id) & (db.Main_Table.id == db.Tag_Table.table_id) & (db.Tag_Table.table_name=="Main_Table") & (db.Tag.id>0)).select(groupby=db.Tag.name)
	for row in x:
		title =  row.Tag.name.replace(" ", "-" )
		url = URL('default', 'tag', args=[title],host=True, extension=False)
		date =  row.Tag.created_on.strftime("%Y-%m-%d")
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n' %(url,date)
	x =  db(db.Event.id > 0 ).select()
	for row in x:
		title = row.name.replace(" ","-")
		url =  URL('default','particular_event', args=[title],host=True, extension=False)
		date =  row.created_on.strftime("%Y-%m-%d")
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n' %(url,date)
	x = db(db.Product.id > 0).select()
	for row in x:
		title = row.name.replace(" ","-")
		url =  URL('function_new','desc_product', args=[title],host=True, extension=False)
		date =  row.created_on.strftime("%Y-%m-%d")
		siteMap += '<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n<changefreq>weekly</changefreq>\n<priority>0.9</priority>\n</url>\n' %(url,date)				
	siteMap += '</urlset>'
	return siteMap
