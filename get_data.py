import wash_data

def get_all_data():
    return wash_data.wash_data()

def select_data(size=1,is_graduate=None,is_married=None,is_female=None,is_self_employed=None,is_urban=None,credit_history=None):
    df=get_all_data()
    df=df.head(int(len(df)*size))
    df=df[df.columns if is_graduate==None else df['Is_graduate']==is_graduate]
    df=df[df.columns if is_female==None else df['Is_Female']==is_female]
    df=df[df.columns if is_self_employed==None else df['Is_self_employed']==is_self_employed]
    df=df[df.columns if is_married==None else df['Is_married']==is_married]
    df=df[df.columns if is_urban==None else df['Is_urban']==is_urban]
    df=df[df.columns if credit_history==None else df['Credit_History']==credit_history]
    return df
