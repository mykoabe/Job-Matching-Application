import { Component, OnInit } from '@angular/core';
import { RestService } from '../Services/rest.service';
import { Works } from '../works';

@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrls: ['./jobs.component.css']
})
export class JobsComponent implements OnInit {

  constructor(private rs: RestService) { }
  headers = ["id", "jobtype", "availability", "status"]
  work : Works[] = [];

  ngOnInit(): void {
    this.rs.readWorks()
    .subscribe
      (
        (response) =>
        {
          this.work = response[0]["data"];
        },
        (error) =>
        {
          console.log("No Data Found" + error);
        }
      )
  }

}
