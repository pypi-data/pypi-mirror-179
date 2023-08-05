import pandas as pd
from pathlib import Path

class Steel_Sections:    
    def __init__(self, section_type: str) -> pd.Series:
        """Returns a pandas df of Canadian steel sections of specified Type, along with it's section properties

        Args:
            section_type (str): Section Type, Allowable inputs: ['2L-EL', '2L-LL', '2L-SL', 'C', 'HP', 'HSS(A500)-REC', 
            'HSS(A500)-ROUND', 'HSS(A500)-SQ', 'HSS(G40)-REC', 'HSS(G40)-ROUND', 'HSS(G40)-SQ', 'L', 'M', 'MC', 'S', 'SLB', 
            'W', 'WRF', 'WT', 'WWF', 'WWT']

        Raises:
            Exception: If the passed `section_type` does not belong to the above categories

        Returns:
            pd.Series: Dataframe with Section Type and Properties
        """
        self.section_type = section_type
        filename = section_type+".pkl"
        filepath = Path(__file__).parent / "sections" / filename
        if filepath.is_file():
            self.list = pd.read_pickle(filepath)
        else:
            raise Exception(f"`{section_type}` is not a valid type. Acceptable Inputs: [{', '.join([x.name.replace('.pkl','') for x in filepath.parent.glob('**/*.pkl')])}]")

    def select_section_by_Dsg(self, Dsg:str) -> pd.Series:
        """Returns a pandas Series that matches the designation
        Args:
            Dsg (str): Beam Metric Designation. Ex: W250x49
        Returns:
            pd.Series: Pandas series with the section properties
        """
        return self.list[self.list['Dsg'] == Dsg].iloc[0,:]

    @staticmethod
    def values_greater_than(df:pd.DataFrame, include_equal:bool =False, **kwargs) -> pd.DataFrame:
        """Takes a pandas dataframe and a dict of col. names as keys and min_val as values. Then returns a filtered dataframe with items whose column values are greater than specified

        Args:
            df (pd.DataFrame): Pandas dataframe to filter down
            include_equal (bool, optional): Include values that are equal to specified values?. Defaults to False.

        Returns:
            pd.DataFrame: Filtered dataframe
        """
        for k, v in kwargs.items():
            if include_equal:
                df = df[df[k] >= v]
            else:
                df = df[df[k] > v]
        return df

    @staticmethod
    def values_lesser_than(df:pd.DataFrame, include_equal:bool =False, **kwargs) -> pd.DataFrame:
        """Takes a pandas dataframe and a dict of col. names as keys and max_val as values. Then returns a filtered dataframe with items whose column values are lesser than specified

        Args:
            df (pd.DataFrame): Pandas dataframe to filter down
            include_equal (bool, optional): Include values that are equal to specified values?. Defaults to False.

        Returns:
            pd.DataFrame: Filtered dataframe
        """
        for k, v in kwargs.items():
            if include_equal:
                df = df[df[k] <= v]
            else:
                df = df[df[k] < v]
        return df

    def rename_list_columns(self, replacement_names:dict) -> None:
        self.list = self.list.rename(columns = replacement_names)
        

    def __repr__(self):
        section_type = self.section_type
        return f"Steel_Sections({section_type=})"

