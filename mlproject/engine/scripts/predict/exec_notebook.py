def run(**kwargs):
    print('####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##############################')
    # if __debug__:
    #     kwargs.update(notebook='irisdataset')
    notebook = kwargs['notebook']
    out_notebook = kwargs['out_notebook']
    import papermill as pm

    pm.execute_notebook(
        notebook,
        out_notebook,
        parameters=dict(file='/opt/airflow/datasets/irisdataset.csv')
    )

# if __debug__:
#     run()