from sqlalchemy.orm.query import Query

class PaginatorService:

    def paginate_base_query(
        self,
        query: Query,
        page: int = 1,
        per_page: int = 10
    ):
        total_items = query.count()
        results = query.offset((page - 1) * per_page).limit(per_page).all()
        items = [
            row._asdict() for row in results
        ]
        response = {
            "data": items,
            "meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": (total_items + per_page - 1) // per_page,
                "total_items": total_items
            }
        }
        return response
