import { Component } from '@angular/core';
import { Vacancy } from '../models/vacancy';
import { ApiService } from '../services/api.service';
@Component({
  selector: 'app-vacancy-list',
  imports: [],
  templateUrl: './vacancy-list.component.html',
  styleUrl: './vacancy-list.component.css'
})
export class VacancyListComponent {
  vacancies:Vacancy[] = [];
  selectedVanacy : Vacancy | null = null;
  constructor(private apiService: ApiService){}
  ngOnInit(): void {
    this.apiService.getVacancies().subscribe( vacancies =>{this.vacancies = vacancies;})
  }
}
