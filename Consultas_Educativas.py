def ProgramsByNumberRegister():
    return """SELECT prg.nombre_prog as nombre_prog, SUM(mat.cant_matriculados) AS cant_matriculados
            FROM programa_academico prg
            INNER JOIN matricula mat
            ON prg.id_prog = mat.id_prog
            GROUP BY prg.nombre_prog
            ORDER BY SUM(mat.cant_matriculados) DESC"""

def InstitutionsByLocation():
    return """SELECT RemoveAccentMarks(dep.nombre_depa) AS nombre_dep, RemoveAccentMarks(mun.nombre_muni) AS nombre_mun, COUNT(inst.nombre_inst) AS cant_inst
            FROM institucion inst
            INNER JOIN municipio mun
            ON inst.id_muni = mun.id_muni
            INNER JOIN departamento dep 
            ON mun.id_depa = dep.id_depa
            GROUP BY dep.nombre_depa, mun.nombre_muni
            ORDER BY dep.nombre_depa, mun.nombre_muni DESC"""

def ProgramsByInstitution():
    return """SELECT inst.id_inst as id_inst, inst.nombre_inst as nombre_inst, COUNT(prg.id_prog) as cant_programas
            FROM institucion inst
            INNER JOIN matricula mat 
            ON inst.id_inst = mat.id_inst
            INNER JOIN programa_academico prg
            ON mat.id_prog = prg.id_prog
            GROUP BY inst.id_inst, inst.nombre_inst
            ORDER BY COUNT(prg.id_prog) DESC"""
            
def StudentsByRegistration():
    return """SELECT mat.anio as anio, mat.semestre as semestre, COUNT(mat.cant_matriculados) as cant_matriculados
            FROM matricula mat
            INNER JOIN programa_academico prg 
            ON mat.id_prog = prg.id_prog
            GROUP BY mat.anio, mat.semestre
            ORDER BY mat.anio, mat.semestre"""

def MaxProgramsByInstitution():
    return """SELECT prg.nombre_prog as nombre_prog, COUNT(inst.id_inst) as cant_inst
            FROM institucion inst 
            INNER JOIN matricula mat 
            ON inst.id_inst = mat.id_inst 
            INNER JOIN programa_academico prg 
            ON mat.id_prog = prg.id_prog 
            GROUP BY prg.nombre_prog
            ORDER BY COUNT(inst.id_inst) DESC"""
            