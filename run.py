import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if '-i' in sys.argv[1]:
            from project import db, create_app
            db.create_all(app=create_app())
    import project
