import difflib

class DynamicNameSearch:
    non_zip_set = set()
    non_zip_mapping = {}
    zip_set = set()
    zip_mapping = {}
    id_type_mapping = {}
    
    @classmethod
    def load_data(cls, queries) -> None:
        for inst in queries:
            search_term = inst.searchname
            
            region_id = inst.regionid
            region_name = inst.regionname
            region_type = inst.regiontype
            cls.id_type_mapping[region_id] = region_type
            st = inst.state
            state = inst.statename
            if region_type == "zip":
                cls.zip_set.add(search_term)
                cls.zip_mapping[search_term] = cls.pack_value(region_id, region_name, region_type, st, state)
            else:
                cls.non_zip_set.add(search_term)
                cls.non_zip_mapping[search_term] = cls.pack_value(region_id, region_name, region_type, st, state)

                
    @classmethod
    def pack_value(cls, region_id, region_name, region_type, st, state) -> dict:
        return {
            "RegionID": region_id,
            "RegionName": region_name,
            "RegionType": region_type,
            "st": st,
            "state": state
        }
    
    @classmethod
    def search(cls, target) -> list:
        try:
            int(target)
            target_arr = difflib.get_close_matches(target.lower(), cls.zip_set)
            return [cls.zip_mapping[word] for word in target_arr]
        except:
            target_arr = difflib.get_close_matches(target.lower(), cls.non_zip_set)
            return [cls.non_zip_mapping[word] for word in target_arr]