from app.database.mongo import positions


def load_positions():

    return list(

        positions.find(

            {},

            {

                "_id": 0

            }

        )

    )


def save_positions(all_positions):

    positions.delete_many({})

    if all_positions:

        positions.insert_many(all_positions)
