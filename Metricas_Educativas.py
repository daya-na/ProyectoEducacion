import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Conexion_Consulta import Connection
import Consultas_Educativas as sql
import plotly.graph_objects as go
from urllib.request import urlopen
import json
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)

external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.1.3/flatly/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# PROGRAMAS EDUCATIVOS POR CANTIDAD DE MATRICULADOS
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ProgramsByNumberRegister(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["nombre_prog", "cant_matriculados"])

# Tabla
figTable = go.Figure()
figTable.add_trace(go.Table(header=dict(
            values=["nombre_prog", "cant_matriculados"],
            font=dict(size=10)
                ),
                cells=dict(
                    values = [dfCases[k].tolist() for k in dfCases.columns[0:]],
                    align = "left"
                    )
                )
            )

# Grafico barras
figBarCases = px.bar(dfCases.head(20), x="nombre_prog", y="cant_matriculados")


# ANALISIS 02: PROPORCIÓN DE INSTITUCIONES POR UBICACIÓN
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.InstitutionsByLocation(), con.connection)
con.closeConnection()
dfInsUb = pd.DataFrame(query, columns=["nombre_dep", "nombre_mun", "cant_inst"])

# Grafico barras
figBarInsUb = px.bar(dfInsUb.head(20), x="nombre_dep", y="cant_inst", color= 'nombre_mun')

# ANALISIS 03: CANTIDAD DE PROGRAMAS ACADÉMICOS BRINDADOS POR INSTITUCIONES
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ProgramsByInstitution(), con.connection)
con.closeConnection()
dfPrgIns = pd.DataFrame(query, columns=["id_inst", "nombre_inst", "cant_programas"])

# Grafico barras
figBardfPrgIns = px.bar(dfPrgIns.head(20), x="nombre_inst", y="cant_programas")

# Tabla
figTablePrgIns = go.Figure()
figTablePrgIns.add_trace(go.Table(header=dict(
            values=["id_inst","nombre_inst", "cant_programas"],
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

# Grafico barras
#figBarfStuReg = px.bar(dfStuReg.head(20), x="anio", y="cant_matriculados")
figBarfStuReg = px.bar(dfStuReg.head(20), x="anio", y="cant_matriculados", color= 'semestre')

# Grafico lineas
figLineStuReg = px.line(dfStuReg.head(20), x="anio", y="cant_matriculados", color='semestre', markers=True)


# ANALISIS 05: PROGRAMAS ACADÉMICOS CON MAYOR PRESENCIA EN INSTITUCIONES
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.MaxProgramsByInstitution(), con.connection)
con.closeConnection()
dfMaPr = pd.DataFrame(query, columns=["nombre_prog", "cant_inst"])

# Grafico barras
figBarfMaPr = px.bar(dfMaPr.head(20), x="nombre_prog", y="cant_inst")

# Grafico pie
figPieMaPr = px.pie(dfMaPr.head(5), names="nombre_prog", values="cant_inst")

# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard Metricas educativas '),
    html.H2(children='Analisis 01: Cantidad de matriculados por programas educativos'),
    dcc.Graph(
          id = 'tableProgramsByNumberRegister',
          figure=figTable
    ), 
    dcc.Graph(
        id='barProgramsByNumberRegister',
        figure=figBarCases
    ),
    html.H2(children='Analisis 02: Proporción de instituciones por ubicación'),
    dcc.Graph(
          id = 'barInstitutionsByLocation',
          figure=figBarInsUb
    ),
    html.H2(children='Analisis 03: Cantidad de programas académicos brindados por institución'),
    dcc.Graph(
        id='tableProgramsByInstitution',
        figure=figTablePrgIns
    ),
    dcc.Graph(
        id='barProgramsByInstitution',
        figure=figBardfPrgIns
    ),
    html.H2(children='Analisis 04: Proporción de alumnos matriculados segun periodo de matricula'),
    dcc.Graph(
        id='barStudentsByRegistration',
        figure=figBarfStuReg
    ),
    dcc.Graph(
        id='lineStudentsByRegistration',
        figure=figLineStuReg
    ),
    html.H2(children='Analisis 05 : Programas académicos con mayor presencia en instituciones'),
    dcc.Graph(
        id='barMaxProgramsByInstitution',
        figure=figBarfMaPr
    ),
    dcc.Graph(
        id='pieMaxProgramsByInstitution',
        figure=figPieMaPr
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)