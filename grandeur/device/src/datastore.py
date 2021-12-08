# This class uses the handlers to provide
# an easy to use api to end users

# Import libraries
from typing import TypeVar
from typing import Callable
from typing import List

# Define subscriber type
# Subscriber = TypeVar('Subscriber')
Collection = TypeVar('Collection')
Pipeline = TypeVar('Pipeline')

class pipeline:

    # Constructor of the class
    def __init__(self, handlers: dict, name: str, index: dict, query: List[dict]):
        # Save handlers in context
        self.handlers = handlers

        # Get reference to the duplex handler
        self.duplex = handlers["duplex"]

        # Store collection name
        self.collection = name

        # Save query and index to context
        self.query = query
        self.index = index

    # Function to add match stage to the query
    def match(self, filter: dict) -> Pipeline:
        # Append the stage to query
        self.query.append({
            "type": "match",
            "filter": filter
        })

        # Return a new pipeline
        return pipeline(self.handlers, self.collection, self.index, self.query)

    # Function to add project stage to the query
    def project(self, specs: dict) -> Pipeline:
        # Append the stage to query
        self.query.append({
            "type": "project",
            "specs": specs
        })

        # Return a new pipeline
        return pipeline(self.handlers, self.collection, self.index, self.query)

    # Function to add group stage to the query
    def group(self, condition: dict, fields: dict) -> Pipeline:
        # Append the stage to query
        self.query.append({
            "type": "group",
            "condition": condition,
            "fields": fields
        })

        # Return a new pipeline
        return pipeline(self.handlers, self.collection, self.index, self.query)

    # Function to add sort stage to the query
    def sort(self, specs: dict) -> Pipeline:
        # Append the stage to query
        self.query.append({
            "type": "sort",
            "specs": specs
        })

        # Return a new pipeline
        return pipeline(self.handlers, self.collection, self.index, self.query)

    # Function to execute the query
    def execute(self, nPage: int, callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "collection": self.collection,
            "index": self.index,
            "pipeline": self.query,
            "nPage": nPage
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/pipeline", payload, callback)


class collection:

    # Constructor of the class
    def __init__(self, handlers: dict, name: str):
        # Save reference to handlers in context
        self.handlers = handlers

        # Get reference to the duplex handler
        self.duplex = handlers["duplex"]

        # Store collection name
        self.collection = name

    # Function to insert data in the collection
    def insert(self, documents: List[dict], callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "collection": self.collection,
            "documents": documents
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/insert", payload, callback)

    # Function to delete documents from the collections
    def delete(self, filter: dict, callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "collection": self.collection,
            "filter": filter
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/delete", payload, callback)

    # Function to update documents from the collections
    def update(self, filter: dict, update: dict, callback: Callable[[str, dict], None]) -> None:
        # Form the request packet
        payload = {
            "collection": self.collection,
            "filter": filter,
            "update": update
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/update", payload, callback)

    # Function to search documents in a collection
    def search(self, filter: dict, project: dict, nPage: int, callback: Callable[[str, dict], None]) -> None:
        # Create a new pipeline and add match stage
        searchPipeline = pipeline(self.handlers, self.collection, {}, []).match(filter)

        # Then append project stage if it is provided
        if project:
            searchPipeline = searchPipeline.project(project)

        # Execute query
        searchPipeline.execute(nPage, callback)
        

    # Function to setup a pipeline
    # It will allow user to stage different quaries and
    # execute together
    def pipeline(self, index: dict) -> Pipeline:
        # Return a new pipeline
        return pipeline(self.handlers, self.collection, index, [])


class datastore:

    # Constructor of the class
    def __init__(self, handlers: dict):
        # Get reference to the duplex handler
        self.handlers = handlers

        # Also store reference to duplex in context
        self.duplex = handlers["duplex"]

    # Function get reference to a collection
    def collection(self, name: str) -> Collection:
        # Return new collection object
        return collection(self.handlers, name)

    # Function to get list of all colelctions
    def list(self, nPage: int, callback: Callable[[str, dict], None]) ->  None:
        # Form the request packet
        payload = {
            "nPage": nPage
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/list", payload, callback)

    # Function to drop a colelction
    def drop(self, name: str, callback: Callable[[str, dict], None]) ->  None:
        # Form the request packet
        payload = {
            "collection": name
        }

        # Send the packet using duplex
        self.duplex.send("/datastore/drop", payload, callback)