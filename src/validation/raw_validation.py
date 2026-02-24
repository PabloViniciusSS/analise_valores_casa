import pandas as pd

class DataValidationError(Exception):
    pass

class RawHousingValidator:
    
    EXPECTED_COLUMNS = [
        "longitude", "latitude", "housing_median_age", "total_rooms",
        "total_bedrooms", "population", "households", "median_income",
        "median_house_value", "ocean_proximity" ]
    

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def validate(self):
        self._check_not_empty()
        self._check_columns()
        self._check_nulls()
        self._check_duplicates()
        self._check_business_rules()
        self._check_ranges()

        print("Validação RAW concluída com sucesso!")


    # ===========================
    # Checks
    # ===========================

    def _check_not_empty(self):
        if self.df.empty:
            raise DataValidationError("O DataFrame está vazio.")  
        
    def _check_columns(self):
        missing = [c for c in self.EXPECTED_COLUMNS if c not in self.df.columns]
        if missing:
            raise DataValidationError(f"Colunas faltando: {missing}")
        

    def _check_nulls(self):
        null_counts = self.df.isnull().sum()

          # total_bedrooms pode ter nulos (já sabemos disso)
        allowed_null_cols = ["total_bedrooms"]

        for col, count in null_counts.items():
            if count > 0 and col not in allowed_null_cols:
                raise DataValidationError(
                    f"Nulos inesperados na coluna {col}"
                )
            
    def _check_duplicates(self):
        if self.df.duplicated().sum() > 0:
            raise DataValidationError("Existem linhas duplicadas no DataFrame.")

    def _check_business_rules(self):
        if(self.df["total_bedrooms"] > self.df["total_rooms"]).any():
            raise DataValidationError(
                "Regra de negócio violada: total_bedrooms não pode ser maior que total_rooms"
            )
        
        if(self.df["median_house_value"] < 0).any():
            raise DataValidationError(
                "Regra de negócio violada: median_house_value não pode ser negativo"
            )
        
        if(self.df["median_income"] < 0).any():
            raise DataValidationError(
                "Regra de negócio violada: median_income não pode ser negativo"
            
            )
        
        if(self.df["housing_median_age"] < 0).any():
            raise DataValidationError(
                "Regra de negócio violada: housing_median_age não pode ser negativo"
            )
        
        if(self.df["population"] < 0).any():
            raise DataValidationError(
                "Regra de negócio violada: population não pode ser negativo"
            )
        
    
        
    def _check_ranges(self):
        if not self.df["longitude"].between(-125, -113).all():
            raise DataValidationError(
                "Valores de longitude fora do range da cidade"
            )
        
        if not self.df["latitude"].between(32, 42).all():
            raise DataValidationError(
                "Valores de latitude fora do range da cidade"
            )
        
        if (self.df["median_income"] <= 0).any():
            raise DataValidationError("median_income inválido.")

        if (self.df["median_house_value"] <= 0).any():
            raise DataValidationError("median_house_value inválido.")
        



