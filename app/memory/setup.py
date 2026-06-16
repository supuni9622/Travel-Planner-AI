from langgraph.checkpoint.postgres import PostgresSaver

DB_URI = (
    "postgresql://travel_user:"
    "travel_password@localhost:5432/travel_ai"
)


def setup_checkpointer():
    with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
        checkpointer.setup()


if __name__ == "__main__":
    setup_checkpointer()