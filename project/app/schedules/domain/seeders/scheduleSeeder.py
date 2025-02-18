from project.app.profesors.domain.ports.profesorsPort import (
    ProfesorPort
)
from project.app.schedules.domain.models.schedulesModel import (
    ScheduleModel
)
from project.shared.domain.ports.seederPort import SeederPort
from project.shared.domain.services.serviceContainer import (
    get_instance
)
from project.shared.domain.utils.updateOrCreate import (
    update_or_create
)


class ScheduleSeeder(SeederPort):

    schedules = [
        {
            "group_id": "560304007-1",
            "subject": "CONMUTACIÓN Y SEÑALIZACIÓN",
            "schedule": "SÁBADO: 6:0-7:59 SÁBADO: 8:0-9:59",
            "classroom": "K-105 FRATERNIDAD MEDELLÍN (32) K-105 FRATERNIDAD MEDELLÍN (32)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "ZULETA GONZÁLEZ LUIS GUILLERMO",
            "identification_card": 71773232
        },
        {
            "group_id": "560304007-2",
            "subject": "CONMUTACIÓN Y SEÑALIZACIÓN",
            "schedule": "JUEVES: 18:0-21:59",
            "classroom": "K-105 FRATERNIDAD MEDELLÍN (32)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "LONDOÑO OSSA IGNACIO ALBERTO",
            "identification_card": 71638947
        },
        {
            "group_id": "560304008-2",
            "subject": "SEÑALES Y SISTEMAS",
            "schedule": "LUNES: 6:0-7:59 MIÉRCOLES: 6:0-7:59",
            "classroom": "N-301 FRATERNIDAD MEDELLÍN (45) N-307 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "BETANCUR PEREZ ANDRES FELIPE",
            "identification_card": 98702799
        },
        {
            "group_id": "560304009-1",
            "subject": "LÍNEAS DE TRASMISIÓN",
            "schedule": "JUEVES: 6:0-7:59 VIERNES: 6:0-7:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40) M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "GONZALEZ VALENCIA ESTEBAN",
            "identification_card": 1128384302
        },
        {
            "group_id": "560304010-1",
            "subject": "SISTEMAS INALÁMBRICOS",
            "schedule": "MIÉRCOLES: 18:0-19:59 VIERNES: 18:0-19:59",
            "classroom": "N-102 FRATERNIDAD MEDELLÍN (32) N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "BETANCUR PEREZ ANDRES FELIPE",
            "identification_card": 98702799
        },
        {
            "group_id": "560506006-1",
            "subject": "REGULACIÓN DE LAS TELECOMUNICACIONES",
            "schedule": "MARTES: 8:0-9:59",
            "classroom": "N-211 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTES GRANADA WILLER FERNEY",
            "identification_card": 15336658
        },
        {
            "group_id": "000202007-1",
            "subject": "INTERNET DE LAS COSAS (I O T)",
            "schedule": "MARTES: 10:0-11:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "REYES VERA ERICK ESTEFEN",
            "identification_card": 1017125415
        },
        {
            "group_id": "000202007-3",
            "subject": "INTERNET DE LAS COSAS (I O T)",
            "schedule": "SÁBADO: 10:0-11:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTOYA CARDONA JORGE ANDRÉS",
            "identification_card": 1216724266
        },
        {
            "group_id": "000202007-6",
            "subject": "INTERNET DE LAS COSAS (I O T)",
            "schedule": "SÁBADO: 12:0-13:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "SOTO PERDOMO JUAN SEBASTIÁN",
            "identification_card": 1079412389
        },
        {
            "group_id": "000202014-3",
            "subject": "INTRODUCCIÓN A LA CIBERSEGURIDAD",
            "schedule": "JUEVES: 18:0-19:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "RODRIGUEZ GIRALDO LUIS FERNANDO",
            "identification_card": 71705938
        },
        {
            "group_id": "000304002-5",
            "subject": "REDES LAN",
            "schedule": "MIÉRCOLES: 8:0-9:59 VIERNES: 8:0-9:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39) Virtual-TEAMS 4 VIRTUAL (100)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "SUAREZ ALVAREZ FABIO LEON",
            "identification_card": 71582563
        },
        {
            "group_id": "000304002-6",
            "subject": "REDES LAN",
            "schedule": "MARTES: 10:0-11:59 JUEVES: 10:0-11:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39) Virtual-TEAMS 2 VIRTUAL (100)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTOYA BENITEZ ALBER OSWALDO",
            "identification_card": 98606628
        },
        {
            "group_id": "000304002-9",
            "subject": "REDES LAN",
            "schedule": "MARTES: 8:0-9:59 JUEVES: 8:0-9:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39) Virtual-TEAMS 3 VIRTUAL (100)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTOYA BENITEZ ALBER OSWALDO",
            "identification_card": 98606628
        },
        {
            "group_id": "000304002-10",
            "subject": "REDES LAN",
            "schedule": "MIÉRCOLES: 20:0-21:59 VIERNES: 20:0-21:59",
            "classroom": "Virtual-TEAMS 15 VIRTUAL (100) N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "SERNA GUARIN LEONARDO",
            "identification_card": 98583374
        },
        {
            "group_id": "000304002-12",
            "subject": "REDES LAN",
            "schedule": "MARTES: 18:0-19:59 JUEVES: 18:0-19:59",
            "classroom": "Virtual-TEAMS 26 VIRTUAL (100) N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "OSPINA CIFUENTES BAYRON JESIT",
            "identification_card": 98565501
        },
        {
            "group_id": "000506001-1",
            "subject": "LÓGICA DE PROGRAMACIÓN Y LABORATORIO",
            "schedule": "MIÉRCOLES: 10:0-11:59 JUEVES: 10:0-11:59 VIERNES: 10:0-11:59",
            "classroom": "N-307 FRATERNIDAD MEDELLÍN (45) K-302 FRATERNIDAD MEDELLÍN (39) K-302 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MORANTES GUZMÁN LUIS JAVIER",
            "identification_card": 88262193
        },
        {
            "group_id": "000506003-3",
            "subject": "CIRCUITOS ELÉCTRICOS I Y LABORATORIO",
            "schedule": "MARTES: 8:0-9:59 JUEVES: 8:0-9:59 VIERNES: 8:0-9:59",
            "classroom": "N-306 FRATERNIDAD MEDELLÍN (45) N-306 FRATERNIDAD MEDELLÍN (45) N-309 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "ESCUDERO QUINTERO CRISTIAN",
            "identification_card": 1017230967
        },
        {
            "group_id": "000506003-6",
            "subject": "CIRCUITOS ELÉCTRICOS I Y LABORATORIO",
            "schedule": "LUNES: 20:0-21:59 MARTES: 20:0-21:59 MIÉRCOLES: 20:0-21:59",
            "classroom": "N-209 FRATERNIDAD MEDELLÍN (45) K-103 FRATERNIDAD MEDELLÍN (25) N-209 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "DURANGO FLOREZ MARIANA",
            "identification_card": 1040745032
        },
        {
            "group_id": "000506005-3",
            "subject": "ELECTRÓNICA ANALÓGICA Y LABORATORIO",
            "schedule": "LUNES: 16:0-17:59 MIÉRCOLES: 16:0-17:59 VIERNES: 16:0-17:59",
            "classroom": "K-103 FRATERNIDAD MEDELLÍN (25) N-302 FRATERNIDAD MEDELLÍN (45) M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "VILLEGAS CEBALLOS JUAN PABLO",
            "identification_card": 1017192320
        },
        {
            "group_id": "000506006-2",
            "subject": "ELECTRÓNICA DIGITAL Y LABORATORIO",
            "schedule": "LUNES: 18:0-19:59 MARTES: 18:0-19:59 MIÉRCOLES: 18:0-19:59",
            "classroom": "O-5 FRATERNIDAD MEDELLÍN (25) O-2 FRATERNIDAD MEDELLÍN (31) Virtual-TEAMS 7 VIRTUAL (100)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "TOBON MEJIA ANDRES FELIPE",
            "identification_card": 71778382
        },
        {
            "group_id": "530202001-101",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "SÁBADO: 6:0-7:59",
            "classroom": "N-309 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "LOPEZ GIRALDO FRANCISCO EUGENIO",
            "identification_card": 98569978
        },
        {
            "group_id": "530202001-102",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "MARTES: 8:0-9:59",
            "classroom": "N-309 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "GARCÍA PINEDA VANESSA",
            "identification_card": 1214718967
        },
        {
            "group_id": "530202001-103",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "JUEVES: 6:0-7:59",
            "classroom": "N-309 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "ARIAS LONDOÑO ALEXANDER",
            "identification_card": 98648261
        },
        {
            "group_id": "530202001-105",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "SÁBADO: 10:0-11:59",
            "classroom": "N-503 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "CASTRILLON FORERO JAVIER ERNESTO",
            "identification_card": 71782916
        },
        {
            "group_id": "530202001-106",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "SÁBADO: 10:0-11:59",
            "classroom": "N-208 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTES GRANADA WILLER FERNEY",
            "identification_card": 15336658
        },
        {
            "group_id": "560202003-1",
            "subject": "INFRAESTRUCTURA DE REDES",
            "schedule": "MIÉRCOLES: 12:0-13:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "SOTO PERDOMO JUAN SEBASTIÁN",
            "identification_card": 1079412389
        },
        {
            "group_id": "560202003-3",
            "subject": "INFRAESTRUCTURA DE REDES",
            "schedule": "MIÉRCOLES: 18:0-19:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "CORTES LÓPEZ CARLOS ALBERTO",
            "identification_card": 88205003
        },
        {
            "group_id": "560202003-4",
            "subject": "INFRAESTRUCTURA DE REDES",
            "schedule": "MIÉRCOLES: 8:0-9:59",
            "classroom": "N-102 FRATERNIDAD MEDELLÍN (32)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "MONTOYA BENITEZ ALBER OSWALDO",
            "identification_card": 98606628
        },
        {
            "group_id": "560202011-1",
            "subject": "FUNDAMENTOS DE COMUNICACIONES INALÁMBRICAS",
            "schedule": "MARTES: 14:00-15:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "OSSA MOLINA OSCAR DAVID",
            "identification_card": 1152195365
        },
        {
            "group_id": "560202012-1",
            "subject": "FUNDAMENTOS DE ANTENAS Y RADIOPROPAGACIÓN",
            "schedule": "JUEVES: 16:00-17:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "LOPEZ GIRALDO FRANCISCO EUGENIO",
            "identification_card": 98569978
        },
        {
            "group_id": "560202013-1",
            "subject": "TELEMÁTICA",
            "schedule": "VIERNES: 8:00-9:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "SERNA GUARIN LEONARDO",
            "identification_card": 98583374
        },
        {
            "group_id": "FPT42-1",
            "subject": "FIBRA ÓPTICA",
            "schedule": "MARTES: 8:00-9:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "GESTIÓN DE REDES DE TELECOMUNICACIONES",
            "instructor": "REYES VERA ERICK ESTEFEN",
            "identification_card": 1017125415
        },
        {
            "group_id": "000202007-2",
            "subject": "INTERNET DE LAS COSAS (IOT)",
            "schedule": "SÁBADO: 10:00-11:59",
            "classroom": "K-501 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "LONDOÑO OSSA IGNACIO ALBERTO",
            "identification_card": 71638947
        },
        {
            "group_id": "000202007-4",
            "subject": "INTERNET DE LAS COSAS (IOT)",
            "schedule": "MIÉRCOLES: 10:00-11:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "REYES VERA ERICK ESTEFEN",
            "identification_card": 1017125415
        },
        {
            "group_id": "000202007-5",
            "subject": "INTERNET DE LAS COSAS (IOT)",
            "schedule": "SÁBADO: 10:00-11:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ZAPATA OCHOA EDISON ANDRES",
            "identification_card": 71796223
        },
        {
            "group_id": "000202007-7",
            "subject": "INTERNET DE LAS COSAS (IOT)",
            "schedule": "VIERNES: 10:00-11:59",
            "classroom": "D-304 ROBLEDO (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "GRAJALES BUSTAMANTE JUAN DAVID",
            "identification_card": 70325806
        },
        {
            "group_id": "000202008-1",
            "subject": "ENERGÍAS RENOVABLES Y SU INSERCIÓN EN LA CUARTA REVOLUCIÓN INDUSTRIAL",
            "schedule": "JUEVES: 10:00-11:59",
            "classroom": "N-315 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CHAMORRO VARILLA DELICIA ESTHER",
            "identification_card": 1128424227
        },
        {
            "group_id": "000202008-2",
            "subject": "ENERGÍAS RENOVABLES Y SU INSERCIÓN EN LA CUARTA REVOLUCIÓN INDUSTRIAL",
            "schedule": "JUEVES: 12:00-13:59",
            "classroom": "N-315 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CHAMORRO VARILLA DELICIA ESTHER",
            "identification_card": 1128424227
        },
        {
            "group_id": "000202008-3",
            "subject": "ENERGÍAS RENOVABLES Y SU INSERCIÓN EN LA CUARTA REVOLUCIÓN INDUSTRIAL",
            "schedule": "LUNES: 16:00-17:59",
            "classroom": "N-404 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CASTRILLON FORERO JAVIER ERNESTO",
            "identification_card": 71782916
        },
        {
            "group_id": "000202009-1",
            "subject": "LA ÓPTICA AL SERVICIO DEL SER HUMANO",
            "schedule": "MARTES: 14:00-15:59",
            "classroom": "M-104 FRATERNIDAD MEDELLÍN (18)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "MARTINEZ CIRO ROGER ALEXANDER",
            "identification_card": 1040260199
        },
        {
            "group_id": "000202014-1",
            "subject": "INTRODUCCIÓN A LA CIBERSEGURIDAD",
            "schedule": "MIÉRCOLES: 10:00-11:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "GRAJALES BUSTAMANTE JUAN DAVID",
            "identification_card": 70325806
        },
        {
            "group_id": "000202014-2",
            "subject": "INTRODUCCIÓN A LA CIBERSEGURIDAD",
            "schedule": "JUEVES: 16:00-17:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "GARCÍA PINEDA VANESSA",
            "identification_card": 1214718967
        },
        {
            "group_id": "000304002-1",
            "subject": "REDES LAN",
            "schedule": "MARTES: 08:00-09:59, JUEVES: 08:00-09:59",
            "classroom": "Virtual-TEAMS 4 VIRTUAL (100), N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "SUAREZ ALVAREZ FABIO LEON",
            "identification_card": 71582563
        },
        {
            "group_id": "000304002-3",
            "subject": "REDES LAN",
            "schedule": "LUNES: 14:00-15:59, MIÉRCOLES: 14:00-15:59",
            "classroom": "Virtual-TEAMS 1 VIRTUAL (100), N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "GRAJALES BUSTAMANTE JUAN DAVID",
            "identification_card": 70325806
        },
        {
            "group_id": "000304002-4",
            "subject": "REDES LAN",
            "schedule": "MIÉRCOLES: 20:00-21:59, VIERNES: 20:00-21:59",
            "classroom": "N-502 FRATERNIDAD MEDELLÍN (39), Virtual-TEAMS 6 VIRTUAL (100)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CORTES LÓPEZ CARLOS ALBERTO",
            "identification_card": 88205003
        },
        {
            "group_id": "000304002-11",
            "subject": "REDES LAN",
            "schedule": "MIÉRCOLES: 20:00-21:59, VIERNES: 20:00-21:59",
            "classroom": "N-102 FRATERNIDAD MEDELLÍN (32), Virtual-TEAMS 13 VIRTUAL (100)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "**NO ASIGNADO**",
            "identification_card": None
        },
        {
            "group_id": "000506001-2",
            "subject": "LÓGICA DE PROGRAMACIÓN Y LABORATORIO",
            "schedule": "LUNES: 08:00-09:59, MIÉRCOLES: 08:00-09:59, VIERNES: 08:00-09:59",
            "classroom": "Virtual-TEAMS 1 VIRTUAL (100), N-306 FRATERNIDAD MEDELLÍN (45), K-404 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ARIAS LONDOÑO ALEXANDER",
            "identification_card": 98648261
        },
        {
            "group_id": "000506001-4",
            "subject": "LÓGICA DE PROGRAMACIÓN Y LABORATORIO",
            "schedule": "LUNES: 18:00-19:59, MIÉRCOLES: 18:00-19:59, VIERNES: 18:00-19:59",
            "classroom": "K-302 FRATERNIDAD MEDELLÍN (39), N-305 FRATERNIDAD MEDELLÍN (45), Virtual-TEAMS 8 VIRTUAL (100)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "VILLA SALAZAR ARLEY FERNANDO",
            "identification_card": 8125602
        },
        {
            "group_id": "000506003-2",
            "subject": "CIRCUITOS ELÉCTRICOS I Y LABORATORIO",
            "schedule": "MARTES: 10:00-11:59, MIÉRCOLES: 10:00-11:59, JUEVES: 10:00-11:59",
            "classroom": "N-306 FRATERNIDAD MEDELLÍN (45), K-103 FRATERNIDAD MEDELLÍN (25), N-306 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "RESTREPO CUESTAS BONIE JOHANA",
            "identification_card": 24694065
        },
        {
            "group_id": "000506003-5",
            "subject": "CIRCUITOS ELÉCTRICOS I Y LABORATORIO",
            "schedule": "MARTES: 18:00-19:59, JUEVES: 18:00-19:59, VIERNES: 18:00-19:59",
            "classroom": "K-103 FRATERNIDAD MEDELLÍN (25), K-104 FRATERNIDAD MEDELLÍN (25), K-104 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "BERMÚDEZ MEJÍA CAMILO ALEJANDRO",
            "identification_card": 1017176876
        },
        {
            "group_id": "000506004-2",
            "subject": "CIRCUITOS ELÉCTRICOS II Y LABORATORIO",
            "schedule": "LUNES: 18:00-19:59, MARTES: 18:00-19:59, JUEVES: 18:00-19:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40), M-109 FRATERNIDAD MEDELLÍN (40), K-302 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ROJAS MONTANO JHON JAIRO",
            "identification_card": 1116917420
        },
        {
            "group_id": "000506005-2",
            "subject": "ELECTRÓNICA ANALÓGICA Y LABORATORIO",
            "schedule": "LUNES: 18:00-19:59, MIÉRCOLES: 18:00-19:59, JUEVES: 18:00-19:59",
            "classroom": "N-302 FRATERNIDAD MEDELLÍN (45), K-103 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "TORRES MUÑOZ FREDY ANDRES",
            "identification_card": 1152436817
        },
        {
            "group_id": "000506006-1",
            "subject": "ELECTRÓNICA DIGITAL Y LABORATORIO",
            "schedule": "LUNES: 8:00-9:59, MIÉRCOLES: 8:00-9:59, VIERNES: 8:00-9:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31), Virtual-TEAMS 26 VIRTUAL (100)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "SERNA GARCES SERGIO IGNACIO",
            "identification_card": 98553427
        },
        {
            "group_id": "530202001-100",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "MIÉRCOLES: 8:00-9:59",
            "classroom": "K-402 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "VALLEJO VALENCIA MARCELA",
            "identification_card": 32182736
        },
        {
            "group_id": "530202001-104",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "JUEVES: 18:00-19:59",
            "classroom": "N-506 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CARMONA CASTRO MAURICIO ALONSO",
            "identification_card": 71675221
        },
        {
            "group_id": "530202001-107",
            "subject": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
            "schedule": "SÁBADO: 14:00-15:59",
            "classroom": "N-206 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "MONTES GRANADA WILLER FERNEY",
            "identification_card": 15336658
        },
        {
            "group_id": "530202008-1",
            "subject": "INSTRUMENTACIÓN INDUSTRIAL",
            "schedule": "MIÉRCOLES: 20:00-21:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CHAMORRO VARILLA DELICIA ESTHER",
            "identification_card": 1128424227
        },
        {
            "group_id": "530202016-1",
            "subject": "DISEÑO Y MONTAJE DE CIRCUITOS Y SISTEMAS ELECTRÓNICOS",
            "schedule": "MIÉRCOLES: 8:00-9:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "CHAMORRO VARILLA DELICIA ESTHER",
            "identification_card": 1128424227
        },
        {
            "group_id": "530202016-2",
            "subject": "FUNDAMENTOS ELECTROMECÁNICOS",
            "schedule": "MIÉRCOLES: 16:00-17:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ALVAREZ SALAZAR JOHNY ANTONIO",
            "identification_card": 98536389
        },
        {
            "group_id": "530202017-1",
            "subject": "ANALÍTICA DE DATOS",
            "schedule": "MIÉRCOLES: 18:00-19:59",
            "classroom": "O-5 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "OSORNO CASTILLO KEVIN",
            "identification_card": 1017273713
        },
        {
            "group_id": "530202018-1",
            "subject": "INTRODUCCIÓN A LA CIENCIA DE DATOS",
            "schedule": "JUEVES: 20:00-21:59",
            "classroom": "N-102 FRATERNIDAD MEDELLÍN (32)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "VALENCIA GARZON SEBASTIAN",
            "identification_card": 1036661748
        },
        {
            "group_id": "530304007-1",
            "subject": "ADQUISICIÓN Y ACONDICIONAMIENTO DE SEÑALES",
            "schedule": "MARTES: 6:00-7:59, JUEVES: 6:00-7:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "VALLEJO VALENCIA MARCELA",
            "identification_card": 32182736
        },
        {
            "group_id": "530304011-1",
            "subject": "ELECTRÓNICA INDUSTRIAL",
            "schedule": "MIÉRCOLES: 18:00-19:59, VIERNES: 18:00-19:59",
            "classroom": "K-103 FRATERNIDAD MEDELLÍN (25), M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ESCUDERO QUINTERO CRISTIAN",
            "identification_card": 1017230967
        },
        {
            "group_id": "530304012-1",
            "subject": "AUTOMATIZACIÓN INDUSTRIAL",
            "schedule": "MARTES: 18:00-19:59, JUEVES: 18:00-19:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "ALVAREZ SALAZAR JOHNY ANTONIO",
            "identification_card": 98536389
        },
        {
            "group_id": "530304013-1",
            "subject": "DISPOSITIVOS PROGRAMABLES",
            "schedule": "MARTES: 20:00-21:59, JUEVES: 20:00-21:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31), Virtual-TEAMS 16 VIRTUAL (100)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "MARTINEZ CIRO ROGER ALEXANDER",
            "identification_card": 1040260199
        },
        {
            "group_id": "XRTC03-1",
            "subject": "TEORÍA DE CONTROL",
            "schedule": "MARTES: 8:00-9:59 JUEVES: 8:00-9:59",
            "classroom": "Virtual-TEAMS 1 VIRTUAL (100) M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "AUTOMATIZACIÓN ELECTRÓNICA",
            "instructor": "DURANGO FLOREZ MARIANA",
            "identification_card": 1040745032
        },
        {
            "group_id": "170202005-100",
            "subject": "FUNDAMENTOS DE ADMINISTRACIÓN",
            "schedule": "JUEVES: 18:00-19:59",
            "classroom": "Virtual-TEAMS 8 VIRTUAL (100)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MARTINEZ OSPINA DANIEL STEVEN",
            "identification_card": 1036652087
        },
        {
            "group_id": "170202016-1",
            "subject": "GESTIÓN DE TIC",
            "schedule": "MARTES: 6:00-7:59 (repetido 18 veces)",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31) Virtual-TEAMS 11 VIRTUAL (100)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GARCÍA PINEDA VANESSA",
            "identification_card": 1214718967
        },
        {
            "group_id": "170202017-1",
            "subject": "FORMULACIÓN Y EVALUACIÓN DE PROYECTOS",
            "schedule": "JUEVES: 18:00-19:59",
            "classroom": "K-402 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "ZULETA GONZÁLEZ LUIS GUILLERMO",
            "identification_card": 71773232
        },
        {
            "group_id": "170202023-1",
            "subject": "SISTEMAS DE AUTOMATIZACIÓN",
            "schedule": "MIÉRCOLES: 10:00-11:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MEJIA ARANGO JUAN GUILLERMO",
            "identification_card": 98514998
        },
        {
            "group_id": "170202024-1",
            "subject": "CONTROL AVANZADO",
            "schedule": "MARTES: 20:00-21:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GOEZ MORA MANUEL MAURICIO",
            "identification_card": 1037603599
        },
        {
            "group_id": "170202025-1",
            "subject": "HERRAMIENTAS DE INTELIGENCIA ARTIFICAL",
            "schedule": "VIERNES: 6:00-7:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "ZULUAGA RIOS CARLOS DAVID",
            "identification_card": 1087985756
        },
        {
            "group_id": "170202025-2",
            "subject": "HERRAMIENTAS DE INTELIGENCIA ARTIFICAL",
            "schedule": "VIERNES: 8:00-9:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "NIETO MORA DANIEL ALEXIS",
            "identification_card": 1017222725
        },
        {
            "group_id": "170202026-1",
            "subject": "INTRODUCCIÓN A LA VISIÓN POR COMPUTADOR",
            "schedule": "VIERNES: 18:00-19:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GOEZ MORA MANUEL MAURICIO",
            "identification_card": 1037603599
        },
        {
            "group_id": "170202027-1",
            "subject": "APRENDIZAJE AUTOMÁTICO EMBEBIDO",
            "schedule": "JUEVES: 18:00-19:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GUARNIZO LEMUS CRISTIAN",
            "identification_card": 10034133
        },
        {
            "group_id": "170304002-1",
            "subject": "CONTROL DIGITAL",
            "schedule": "LUNES: 20:00-21:59, JUEVES: 20:00-21:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40), M-104 FRATERNIDAD MEDELLÍN (18)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "ROJAS MONTANO JHON JAIRO",
            "identification_card": 1116917420
        },
        {
            "group_id": "170304004-2",
            "subject": "PROGRAMACIÓN AVANZADA",
            "schedule": "MIÉRCOLES: 20:00-21:59, VIERNES: 20:00-21:59",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31), Virtual-TEAMS 26 VIRTUAL (100)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GUARNIZO LEMUS CRISTIAN",
            "identification_card": 10034133
        },
        {
            "group_id": "170304008-1",
            "subject": "TEORÍA ELECTROMAGNÉTICA",
            "schedule": "MARTES: 6:00-7:59, JUEVES: 6:00-7:59",
            "classroom": "N-302 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "PÉREZ WALTON SANTIAGO",
            "identification_card": 71375387
        },
        {
            "group_id": "170304009-1",
            "subject": "OPTIMIZACIÓN",
            "schedule": "MARTES: 16:00-17:59, JUEVES: 16:00-17:59",
            "classroom": "O-5 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GUARNIZO LEMUS CRISTIAN",
            "identification_card": 10034133
        },
        {
            "group_id": "170304012-1",
            "subject": "SISTEMAS DIGITALES AVANZADOS",
            "schedule": "MARTES: 16:00-17:59, JUEVES: 16:00-17:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MARQUEZ VILORIA DAVID ANDRES",
            "identification_card": 16079570
        },
        {
            "group_id": "170304014-1",
            "subject": "PROCESAMIENTO DIGITAL DE SEÑALES",
            "schedule": "MARTES: 18:00-19:59, JUEVES: 18:00-19:59",
            "classroom": "O-5 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "ROLDAN VASCO SEBASTIAN",
            "identification_card": 1037570818
        },
        {
            "group_id": "170304019-1",
            "subject": "INTELIGENCIA ARTIFICIAL",
            "schedule": "MIÉRCOLES: 6:00-7:59, VIERNES: 6:00-7:59",
            "classroom": "Virtual-TEAMS 3 VIRTUAL (100), O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "NIETO MORA DANIEL ALEXIS",
            "identification_card": 1017222725
        },
        {
            "group_id": "170304020-1",
            "subject": "MÁQUINAS ELÉCTRICAS",
            "schedule": "LUNES: 20:00-21:59, MARTES: 20:00-21:59",
            "classroom": "G-204 ROBLEDO (24), Virtual-TEAMS 6 VIRTUAL (100)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MEJIA ARANGO JUAN GUILLERMO",
            "identification_card": 98514998
        },
        {
            "group_id": "CAW104-2",
            "subject": "CONTROL APLICADO",
            "schedule": "SÁBADO: 14:00-15:59, SÁBADO: 16:00-17:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "BERMÚDEZ MEJÍA CAMILO ALEJANDRO",
            "identification_card": 1017176876
        },
        {
            "group_id": "DDW103-2",
            "subject": "DISEÑO DIGITAL",
            "schedule": "MARTES: 18:00-19:59, JUEVES: 18:00-19:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24), K-405 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MARQUEZ VILORIA DAVID ANDRES",
            "identification_card": 16079570
        },
        {
            "group_id": "EPW103-1",
            "subject": "ELECTRÓNICA DE POTENCIA",
            "schedule": "MIÉRCOLES: 18:00-19:59, VIERNES: 18:00-19:59",
            "classroom": "M-109 FRATERNIDAD MEDELLÍN (40), K-103 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "VILLEGAS CEBALLOS JUAN PABLO",
            "identification_card": 1017192320
        },
        {
            "group_id": "IAW102-1",
            "subject": "INTELIGENCIA ARTIFICIAL II",
            "schedule": "JUEVES: 18:00-19:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "OSORNO CASTILLO KEVIN",
            "identification_card": 1017273713
        },
        {
            "group_id": "IEW93-1",
            "subject": "INSTRUMENTACIÓN ELECTRÓNICA",
            "schedule": "MIÉRCOLES: 20:00-21:59, VIERNES: 20:00-21:59",
            "classroom": "M-110 FRATERNIDAD MEDELLÍN (40), M-109 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "GOEZ MORA MANUEL MAURICIO",
            "identification_card": 1037603599
        },
        {
            "group_id": "LPW72-1",
            "subject": "LENGUAJES DE PROGRAMACIÓN",
            "schedule": "MARTES: 18:00-19:59, MIÉRCOLES: 18:00-19:59",
            "classroom": "Virtual-TEAMS 6 VIRTUAL (100), N-402 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "NIETO MORA DANIEL ALEXIS",
            "identification_card": 1017222725
        },
        {
            "group_id": "MCW93-1",
            "subject": "MICROELECTRÓNICA",
            "schedule": "MARTES: 16:00-17:59, MIÉRCOLES: 16:00-17:59",
            "classroom": "O-2 FRATERNIDAD MEDELLÍN (31), O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "DURANGO FLOREZ MARIANA",
            "identification_card": 1040745032
        },
        {
            "group_id": "MEW93-3",
            "subject": "MÁQUINAS ELÉCTRICAS",
            "schedule": "MARTES: 18:00-19:59, VIERNES: 18:00-19:59",
            "classroom": "Virtual-TEAMS 2 VIRTUAL (100), G-204 ROBLEDO (24)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "MEJIA ARANGO JUAN GUILLERMO",
            "identification_card": 98514998
        },
        {
            "group_id": "TEW83-1",
            "subject": "TEORÍA ELECTROMAGNÉTICA",
            "schedule": "MARTES: 20:00-21:59, JUEVES: 20:00-21:59",
            "classroom": "N-302 FRATERNIDAD MEDELLÍN (45), N-302 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA ELECTRÓNICA",
            "instructor": "ARIAS GARZON ANDRES FELIPE",
            "identification_card": 71385588
        },
        {
            "group_id": "170202011-1",
            "subject": "SEMINARIO DE INVESTIGACIÓN",
            "schedule": "LUNES: 18:00-19:59",
            "classroom": "K-405 FRATERNIDAD MEDELLÍN (40)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "CARMONA CASTRO MAURICIO ALONSO",
            "identification_card": 71675221
        },
        {
            "group_id": "210202001-1",
            "subject": "TÓPICOS AVANZADOS EN ANTENAS PATCH",
            "schedule": "JUEVES: 8:00-9:59 (18 veces)",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24) (18 veces)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "LOPEZ GIRALDO FRANCISCO EUGENIO",
            "identification_card": 98569978
        },
        {
            "group_id": "210202003-1",
            "subject": "COMUNICACIÓN POR LUZ VISIBLE II",
            "schedule": "VIERNES: 6:00-7:59",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "MARTINEZ CIRO ROGER ALEXANDER",
            "identification_card": 1040260199
        },
        {
            "group_id": "210304012-1",
            "subject": "COMUNICACIONES DIGITALES",
            "schedule": "LUNES: 20:0-21:59 MIÉRCOLES: 20:0-21:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24) O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "BETANCUR PEREZ ANDRES FELIPE",
            "identification_card": 98702799
        },
        {
            "group_id": "210304013-1",
            "subject": "COMUNICACIONES ÓPTICAS",
            "schedule": "LUNES: 18:0-19:59 MIÉRCOLES: 18:0-19:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24) O-2 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "GOMEZ CARDONA NELSON DARIO",
            "identification_card": 71779814
        },
        {
            "group_id": "210304015-1",
            "subject": "ANTENAS",
            "schedule": "MIÉRCOLES: 16:0-17:59 VIERNES: 16:0-17:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24) N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "YEPES ZULUAGA SARA MARIA",
            "identification_card": 43165096
        },
        {
            "group_id": "210304019-1",
            "subject": "RADIOCOMUNICACIONES",
            "schedule": "MIÉRCOLES: 18:0-19:59 VIERNES: 18:0-19:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24) N-504 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "OSSA MOLINA OSCAR DAVID",
            "identification_card": 1152195365
        },
        {
            "group_id": "ART82-2",
            "subject": "ADMINISTRACIÓN DE REDES",
            "schedule": "MARTES: 20:0-21:59",
            "classroom": "Virtual-TEAMS 1 VIRTUAL (100)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "OSPINA CIFUENTES BAYRON JESIT",
            "identification_card": 98565501
        },
        {
            "group_id": "COLUZVIS02-1",
            "subject": "COMUNICACIÓN POR LUZ VISIBLE I",
            "schedule": "MIÉRCOLES: 6:0-7:59",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "MARTINEZ CIRO ROGER ALEXANDER",
            "identification_card": 1040260199
        },
        {
            "group_id": "DIANPAT02-1",
            "subject": "DISEÑO DE ANTENAS PATCH",
            "schedule": "MARTES: 20:0-21:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "OSSA MOLINA OSCAR DAVID",
            "identification_card": 1152195365
        },
        {
            "group_id": "FEX03-1",
            "subject": "FORMULACIÓN, EVALUACIÓN Y CONTROL DE PROYECTOS",
            "schedule": "LUNES: 6:0-7:59 JUEVES: 6:0-7:59",
            "classroom": "Virtual-TEAMS 4 VIRTUAL (100) N-204 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "MARTINEZ OSPINA DANIEL STEVEN",
            "identification_card": 1036652087
        },
        {
            "group_id": "GTT103-2",
            "subject": "GESTIÓN TECNOLÓGICA",
            "schedule": "MIÉRCOLES: 20:0-21:59 VIERNES: 20:0-21:59",
            "classroom": "N-315 FRATERNIDAD MEDELLÍN (45) N-404 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "LEZCANO RODRÍGUEZ LUIS ALFONSO",
            "identification_card": 71185161
        },
        {
            "group_id": "IIX01-2",
            "subject": "INTRODUCCIÓN A LA INVESTIGACIÓN",
            "schedule": "MARTES: 20:0-21:59",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "CASTRILLON FORERO JAVIER ERNESTO",
            "identification_card": 71782916
        },
        {
            "group_id": "IIX01-3",
            "subject": "INTRODUCCIÓN A LA INVESTIGACIÓN",
            "schedule": "VIERNES: 16:0-17:59",
            "classroom": "N-402 FRATERNIDAD MEDELLÍN (31)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "MONCADA ACEVEDO MARIA ELENA",
            "identification_card": 43629910
        },
        {
            "group_id": "LTT93-1",
            "subject": "LÍNEAS DE TRANSMISIÓN",
            "schedule": "MARTES: 18:0-19:59 JUEVES: 18:0-19:59",
            "classroom": "K-105 FRATERNIDAD MEDELLÍN (32) N-307 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "MONTES GRANADA WILLER FERNEY",
            "identification_card": 15336658
        },
        {
            "group_id": "PST104-3",
            "subject": "PROCESAMIENTO DE SEÑALES II",
            "schedule": "MARTES: 6:0-7:59 SÁBADO: 6:0-7:59",
            "classroom": "K-402 FRATERNIDAD MEDELLÍN (39) K-304 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "NIETO MORA DANIEL ALEXIS",
            "identification_card": 1017222725
        },
        {
            "group_id": "PST93-1",
            "subject": "PROCESAMIENTO DE SEÑALES I",
            "schedule": "MARTES: 20:0-21:59 JUEVES: 20:0-21:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24) N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "ROLDAN VASCO SEBASTIAN",
            "identification_card": 1037570818
        },
        {
            "group_id": "RCT104-2",
            "subject": "RADIOCOMUNICACIONES",
            "schedule": "LUNES: 18:0-19:59 MIÉRCOLES: 18:0-19:59 VIERNES: 18:0-19:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24) M-110 FRATERNIDAD MEDELLÍN (40) K-404 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "ZAPATA OCHOA EDISON ANDRES",
            "identification_card": 71796223
        },
        {
            "group_id": "RCT93-3",
            "subject": "REDES DE COMUNICACIONES",
            "schedule": "MIÉRCOLES: 18:0-19:59 VIERNES: 18:0-19:59",
            "classroom": "L-401 FRATERNIDAD MEDELLÍN (25) N-502 FRATERNIDAD MEDELLÍN (39)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "LEZCANO RODRÍGUEZ LUIS ALFONSO",
            "identification_card": 71185161
        },
        {
            "group_id": "RPT102-2",
            "subject": "REDES DE PRÓXIMA GENERACIÓN",
            "schedule": "MARTES: 20:0-21:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "NAVARRO RESTREPO JUAN DAVID",
            "identification_card": 1017207746
        },
        {
            "group_id": "STT101-1",
            "subject": "SEMINARIO DE TELECOMUNICACIONES",
            "schedule": "JUEVES: 20:0-21:59",
            "classroom": "N-309 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "LEZCANO RODRÍGUEZ LUIS ALFONSO",
            "identification_card": 71185161
        },
        {
            "group_id": "TCT92-1",
            "subject": "TECNOLOGÍAS CONVERGENTES",
            "schedule": "MIÉRCOLES: 20:0-21:59",
            "classroom": "N-101 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "NAVARRO RESTREPO JUAN DAVID",
            "identification_card": 1017207746
        },
        {
            "group_id": "TET83-3",
            "subject": "TEORÍA ELECTROMAGNÉTICA",
            "schedule": "MARTES: 18:0-19:59 JUEVES: 18:0-19:59",
            "classroom": "N-315 FRATERNIDAD MEDELLÍN (45) N-315 FRATERNIDAD MEDELLÍN (45)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "ORREGO RESTREPO ESTEFANIA",
            "identification_card": 1036944138
        },
        {
            "group_id": "TTT83-2",
            "subject": "TEORÍA DE TELETRÁFICO",
            "schedule": "SÁBADO: 6:0-7:59 SÁBADO: 8:0-9:59",
            "classroom": "O-1 FRATERNIDAD MEDELLÍN (24) O-1 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "INGENIERÍA DE TELECOMUNICACIONES",
            "instructor": "LONDOÑO OSSA IGNACIO ALBERTO",
            "identification_card": 71638947
        },
        {
            "group_id": "ART64-4",
            "subject": "ANTENAS Y RADIOPROPAGACIÓN",
            "schedule": "MARTES: 18:0-19:59 JUEVES: 18:0-19:59",
            "classroom": "N-302 FRATERNIDAD MEDELLÍN (45) N-501 FRATERNIDAD MEDELLÍN (24)",
            "academic_program": "TELECOMUNICACIONES",
            "instructor": "SOTO PERDOMO JUAN SEBASTIÁN",
            "identification_card": 1079412389
        },
        {
            "group_id": "MTT52-2",
            "subject": "MEDIOS DE TRANSMISIÓN",
            "schedule": "MARTES: 18:0-19:59 MIÉRCOLES: 18:0-18:59",
            "classroom": "N-501 FRATERNIDAD MEDELLÍN (24) K-105 FRATERNIDAD MEDELLÍN (32)",
            "academic_program": "TELECOMUNICACIONES",
            "instructor": "GONZALEZ VALENCIA ESTEBAN",
            "identification_card": 1128384302
        },
        {
            "group_id": "RTT62-1",
            "subject": "REDES DE TELECOMUNICACIONES",
            "schedule": "LUNES: 20:0-21:59",
            "classroom": "O-5 FRATERNIDAD MEDELLÍN (25)",
            "academic_program": "TELECOMUNICACIONES",
            "instructor": "RODRIGUEZ GIRALDO LUIS FERNANDO",
            "identification_card": 71705938
        }
    ]


    def handle(self):
        try:
            profesor_not_found = []
            profesor_port = get_instance(ProfesorPort)
            for schedule in self.schedules:
                get_profesor = profesor_port.get_profesor_by_identification_card(
                    identification_card=schedule.get("identification_card")
                )
                if not get_profesor:
                    if  schedule.get("identification_card") not in profesor_not_found:
                        profesor_not_found.append(schedule.get("identification_card"))
                    continue
                schedule.pop("instructor")
                schedule.pop("identification_card")
                schedule.update({"profesor_id": get_profesor.id})
                update_or_create(
                    session=self.session,
                    model=ScheduleModel,
                    keys={
                        "group_id": schedule.get("group_id")
                    },
                    data=schedule
                )
            print(profesor_not_found)
        except Exception as error:
            self.session.rollback()
            print(f"Error in the Seeder ProfesorSeeder: {error}")
        finally:
            self.session.close()
