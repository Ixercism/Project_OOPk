from src.headhunterapi import HeadhunterAPI
from src.jsonvacancystorage import JSONVacancyStorage
from src.vacancy import Vacancy


def main():
    job_title = input("Введите название вакансии: ")
    top_vacancy = int(
        input("Введите сколько вакансий, отсортированных по зарплате вам нужно: ")
    )

    hh_api = HeadhunterAPI()
    raw_vacancies = hh_api.get_vacancies(job_title, top_vacancy)
    storage = JSONVacancyStorage("sample.json")

    vacancies = []

    for item in raw_vacancies:
        salary_dict = item.get("salary")
        if salary_dict is not None:
            salary = salary_dict.get("from")
            if salary is None:
                salary = 0
        else:
            salary = 0
        vac_obj = Vacancy(item["name"], item["alternate_url"], salary, item["snippet"])
        vacancies.append(vac_obj)

    sorted_vacancies = sorted(vacancies)
    storage.save_to_file(sorted_vacancies)

    for i in sorted_vacancies:
        print(i.__dict__)


if __name__ == "__main__":
    main()
