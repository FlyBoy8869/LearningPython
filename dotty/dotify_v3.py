"""
namespace(product='Korean CECIL3 Lance Barrel',
          drawings=namespace(e0=namespace(kind='assembly',
                                          number='P0800150790',
                                          title='Spring Motor',
                                          status='active',
                                          notes=''),
                             e1=namespace(kind='assembly',
                                          number='P0800150791',
                                          title='Modification, Spring Motor',
                                          status='active',
                                          notes="Tap holes to 1/4-20, don't "
                                                'drill'),
                             e2=namespace(kind='part',
                                          number='P0800150788',
                                          title='Plate, Base, Springs, Take Up',
                                          status='active',
                                          notes=''),
                             e3=namespace(kind='part',
                                          number='P0800150789',
                                          title='Spacer, Springs, Take Up',
                                          status='active',
                                          notes=''),
                             e4=namespace(kind='part',
                                          number='P0800150822',
                                          title='Modification, Stopper',
                                          status='active',
                                          notes=''),
                             e5=namespace(kind='part',
                                          number='P0800150823',
                                          title='Washer, Spring Motor',
                                          status='active',
                                          notes=''),
                             e6=namespace(kind='part',
                                          number='P0800150824',
                                          title='Bar, Cables, Spring Motor',
                                          status='active',
                                          notes=''),
                             e7=namespace(kind='part',
                                          number='P0800150839',
                                          title='Cover, Springs, Take Up',
                                          status='active',
                                          notes='')),
          documents=namespace(e0=namespace(number='DKEP.CECIL3.315',
                                           title='Bench Top Test - Spring '
                                                 'Motors',
                                           status='active',
                                           notes=''),
                              e1=namespace(number='DKEP.CECIL3.2016',
                                           title='Assembly, Spring Motor '
                                                 'Take-Up, Traveler',
                                           status='active',
                                           notes='')),
          author='Charles Cognato')

"""
from types import SimpleNamespace


class DotifyObject:
    def __init__(self, obj):
        self._list_number = self._list_counter()
        self._dict_number = self._dict_counter()
        self._data = self.dotify_object(obj)

    @property
    def data(self):
        return self._data

    @staticmethod
    def _list_counter():
        list_start = 0
        while True:
            yield list_start
            list_start += 1

    @staticmethod
    def _dict_counter():
        dict_start = 0
        while True:
            yield dict_start
            dict_start += 1

    def dotify_object(self, object_to_dotify):
        ns = None

        if isinstance(object_to_dotify, dict):
            ns = self.dotify_dictionary(object_to_dotify)
        elif isinstance(object_to_dotify, list):
            ns = self.dotify_list(object_to_dotify)

        return ns

    def dotify_list(self, list_to_dotify: list):
        namespace = SimpleNamespace()

        for index, element in enumerate(list_to_dotify):
            if isinstance(element, dict):
                ns = self.dotify_dictionary(element)
                # setattr(namespace, f"dict{index}", ns)
                setattr(namespace, f"dict{next(self._dict_number)}", ns)
            elif isinstance(element, list):
                ns = self.dotify_list(element)
                setattr(namespace, f"list{next(self._list_number)}", ns)
            else:
                setattr(namespace, f"element{index}", element)

        return namespace

    def dotify_dictionary(self, dict_to_dotify: dict):
        namespace = SimpleNamespace()
        for key, value in dict_to_dotify.items():
            if isinstance(value, dict):
                ns = self.dotify_dictionary(value)
                setattr(namespace, key, ns)
            elif isinstance(value, list):
                ns = self.dotify_list(value)
                setattr(namespace, key, ns)
            else:
                setattr(namespace, key, value)

        return namespace


class DottedAssembly:
    """
    Parameters:
        title       :str: assembly nomenclature
        drawings    :SimpleNamespace: drawings for assembly
        documents   :SimpleNamespace: documents for assembly

    note: doesn't handle lists within lists.

    modified 05/31/2024
    """

    def __init__(self, *, title=None, drawings=None, documents=None):
        self.title = title
        self.drawings = drawings
        self.documents = documents

    @classmethod
    def assembly_from_json_object(cls, json_object):
        djson = DotifyObject(json_object)
        return cls(
            title=djson.data.title,
            drawings=djson.data.drawings,
            documents=djson.data.documents
        )

    @property
    def drawing_count(self):
        return len(vars(self.drawings))

    @property
    def document_count(self):
        return len(vars(self.documents))

    def _set_items(self, obj):
        for item in [member for member in obj.__dict__ if not member.startswith("_")]:
            setattr(self, item, obj.__dict__[item])

    def items(self, section=None):
        if section:
            return {k: v for k, v in section.__dict__.items() if not k.startswith("_")}
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def iter_drawings(self):
        yield from self._iter_items(self.drawings)

    def iter_documents(self):
        yield from self._iter_items(self.documents)

    @staticmethod
    def _iter_items(item):
        for i in vars(item):
            yield getattr(item, i)


if __name__ == "__main__":
    import json
    from pprint import pprint

    with open("spring_motor.json", "rb") as infile:
        jdata = json.load(infile)

    assembly = DottedAssembly.assembly_from_json_object(jdata)

    dobj = DotifyObject(jdata)
    pprint(dobj.data)
    # print(dobj.drawings.dict1.notes)

    l = [
        "element0",
        [
            "one", "two", "three", "four", "five"
        ],
        "element2",
        [
            "six", {"donkey": "male"}, "seven", "eight", "nine", "ten"
        ]
    ]

    dobj1 = DotifyObject(l)
    pprint(dobj1.data)
