from professorUFS import ProfessorUFS


def main():
    professor = ProfessorUFS('Andreia', 5, 10)

    print(professor.getCargaHrSemanal())
    professor.maisHoras(15)
    print(professor.getCargaHrSemanal())
    professor.menosHoras(10)
    print(professor.getCargaHrSemanal())
    professor.menosHoras(20)
    print(professor.getCargaHrSemanal())


if __name__ == '__main__':
    main()
