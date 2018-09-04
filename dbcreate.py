from scraping import contents
import dbsetting as dbs

#DB作成（すでに存在する場合は無視される）
dbs.Base.metadata.create_all(dbs.conn)

#scrapingしてきたデータをDBの形式に変換
records = [dbs.LinkRecord(content) for content in contents]

#DB作成
dbs.session.query(dbs.LinkRecord).delete()
dbs.session.add_all(records)
dbs.session.commit()
