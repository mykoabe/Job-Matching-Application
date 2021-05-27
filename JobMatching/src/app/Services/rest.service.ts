import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Employee } from '../Emoloyee';

@Injectable({
  providedIn: 'root'
})
export class RestService implements OnInit {

  constructor(private http : HttpClient) { }

  ngOnInit(){
  }

  employeeUrl : string = "http://127.0.0.1:5000/employeeReport/";

  readEmployee()
  {
    return this.http.get<Employee[]>(this.employeeUrl);
  }
}
