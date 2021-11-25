import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Conexion_Consulta import Connection
import Consultas_Educativas as sql
import plotly.graph_objects as go

external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.1.3/flatly/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# ANALISIS 01: PROGRAMAS EDUCATIVOS POR CANTIDAD DE MATRICULADOS
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ProgramsByNumberRegister(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=[ "nombre_prog", "cant_matriculados"])

# Tabla
figTable = go.Figure()
figTable.add_trace(go.Table(header=dict( 
            values=[ "nombre_prog", "cant_matriculados"],
            font=dict(size=10)
                ),
                cells=dict(
                    values = [dfCases[k].tolist() for k in dfCases.columns[0:]],
                    align = "left"
                    )
                )
            )

# Grafico barras Vertical 
figBarCases = px.bar(dfCases.head(10), y="nombre_prog", x="cant_matriculados", orientation='h')


# ANALISIS 02: PROPORCIÓN DE INSTITUCIONES POR UBICACIÓN
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.InstitutionsByLocation(), con.connection)
con.closeConnection()
dfInsUb = pd.DataFrame(query, columns=["nombre_dep", "nombre_mun", "cant_inst"])

# Grafico barras vertical
figBarInsUb = px.bar(dfInsUb.head(20), y="nombre_dep", x="cant_inst", color= 'nombre_mun', orientation='h')

# ANALISIS 03: CANTIDAD DE PROGRAMAS ACADÉMICOS BRINDADOS POR INSTITUCIONES SEGUN NIVEL ACADEMICO
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ProgramsByInstitution(), con.connection)
con.closeConnection()
#dfPrgIns = pd.DataFrame(query, columns=["nombre_inst", "nivel_academico", "cant_programas"])
dfPrgIns = pd.DataFrame(query, columns=["nombre_inst", "nivel_academico", "cant_programas"])

# Grafico barras vertical
figBardfPrgIns = px.bar(dfPrgIns.head(10), y="nombre_inst", x="cant_programas", orientation='h', color="nivel_academico")


# Tabla
figTablePrgIns = go.Figure()
figTablePrgIns.add_trace(go.Table(header=dict(
            values=["nombre_inst", "nivel_academico", "cant_programas"],
            font=dict(size=10)
                ),
                cells=dict(
                    values = [dfPrgIns[k].tolist() for k in dfPrgIns.columns[0:]],
                    align = "left"
                    )
                )
            )


# ANALISIS 04: PROPORCIÓN DE ALUMNOS MATRICULADOS SEGUN PERIODO DE MATRICULA
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.StudentsByRegistration(), con.connection)
con.closeConnection()
dfStuReg = pd.DataFrame(query, columns=["anio", "semestre", "cant_matriculados"])

# Grafico de pie
figBarfStuReg = px.pie(dfStuReg.head(12), names="anio", values="cant_matriculados")


# Grafico lineas
figLineStuReg = px.line(dfStuReg.head(20), x="anio", y="cant_matriculados", color='semestre', markers=True)


# ANALISIS 05: PROGRAMAS ACADÉMICOS CON MAYOR PRESENCIA EN INSTITUCIONES
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.MaxProgramsByInstitution(), con.connection)
con.closeConnection()
dfMaPr = pd.DataFrame(query, columns=["nombre_prog", "cant_inst"])

# Grafico barras horizontal
figBarfMaPr = px.bar(dfMaPr.head(20), x="nombre_prog", y="cant_inst")

# Grafico pie
figPieMaPr = px.pie(dfMaPr.head(5), names="nombre_prog", values="cant_inst")

# Layout 
app.layout = html.Div(children=[
    html.H1(className ="container-fluid bg-primary text-white text-center p-4" ,children='Dashboard Metricas educativas '),
    
    #Container para el ancho completo 
    html.Div(className="container-fluid", children=[
        html.H3(className="p-3", children='Analisis 01: Cantidad de matriculados por programas educativos'),
        # Filas para los casos 
        html.Div(className="row", children=[
            # columna para barras verticales 
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header", children=[
                        html.H6(children='Tabla de programas academicos y cantidad de matriculados'),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                  id = 'tableProgramsByNumberRegister',
                                  figure=figTable
                            ),
                            ])
                    ])
                ]),
            # columna para barras verticales 
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H6(children='Grafico de barras de programas academicos y cantidad de matriculados'),
                            ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='barProgramsByNumberRegister',
                                figure=figBarCases
                            ),
                            ])
                        ])
                    ])
            ])
        ]),
     #Container para el ancho completo 
    html.Div(className="container-fluid", children=[
        html.H3(className="p-3",children='Analisis 02: Proporción de instituciones por ubicación'),
        # Filas para los casos 
        html.Div(className="row", children=[
            # columna para barras verticales 
            html.Div(className="col-12 col-xl-12", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header", children=[
                        html.H6(children='Grafico de barras de Proporción de instituciones por ubicación'),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                  id = 'barInstitutionsByLocation',
                                  figure=figBarInsUb
                            ),
                            ])
                    ])
                ])
            ])
        ]),
    #Container para el ancho completo 
    html.Div(className="container-fluid", children=[
        html.H3(className="p-3",children='Analisis 03: Cantidad de programas académicos brindados por institución según nivel academico'),
        # Filas para los casos 
        html.Div(className="row", children=[
            # columna para barras verticales 
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header", children=[
                        html.H6(children='Tabla de programas academicos y cantidad de matriculados'),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='tableProgramsByInstitution',
                                figure=figTablePrgIns
                            ),
                            ])
                    ])
                ]),
            # columna para barras verticales 
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H6(children='Grafico de barras de programas academicos y cantidad de matriculados'),
                            ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='barProgramsByInstitution',
                                figure=figBardfPrgIns
                            ),
                            ])
                        ])
                    ])
            ])
        ]),
    #Container para el ancho completo 
    html.Div(className="container-fluid", children=[
        html.H3(className="p-3",children='Analisis 04: Proporción de alumnos matriculados segun periodo de matricula'),
        # Filas para los casos 
        html.Div(className="row", children=[
            # columna para barras verticales 
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header", children=[
                        html.H6(children='Grafico de pie de programas academicos y cantidad de matriculados'),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='barStudentsByRegistration',
                                figure=figBarfStuReg
                            ),
                            ])
                    ])
                ]),
            # columna para barras verticales 
                html.Div(className="col-12 col-xl-6", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H6(children='Grafico de lineas de programas academicos y cantidad de matriculados'),
                            ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='lineStudentsByRegistration',
                                figure=figLineStuReg
                            ),
                            ])
                        ])
                    ])
            ])
        ]),
      #Container para el ancho completo 
    html.Div(className="container-fluid", children=[
        html.H3(className="p-3",children='Analisis 05 : Programas académicos con mayor presencia en instituciones'),
        # Filas para los casos 
        html.Div(className="row", children=[
            # columna para barras verticales 
            html.Div(className="col-12 col-xl-6", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header", children=[
                        html.H6(children='Grafico de barras de programas academicos y cantidad de matriculados'),
                        ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='barMaxProgramsByInstitution',
                                figure=figBarfMaPr
                            ),
                            ])
                    ])
                ]),
            # columna para barras verticales 
                html.Div(className="col-12 col-xl-6 pb-5", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H6(children='Grafico de pie de programas academicos y cantidad de matriculados'),
                            ]),
                        html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='pieMaxProgramsByInstitution',
                                figure=figPieMaPr
                            )
                            ])
                        ])
                    ])
            ])
        ])
    
])


if __name__ == '__main__':
    app.run_server(debug=True)
