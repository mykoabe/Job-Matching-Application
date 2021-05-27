import { Component, OnInit } from '@angular/core';
import { RestService } from './Services/rest.service';
import { Employee } from './Emoloyee';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Job Matching';

  constructor(private rs : RestService){}
  headers = ["id","empName", "Age",  "Description"]

  employee : Employee[] = [];

  ngOnInit()
  {
      this.rs.readEmployee()
      .subscribe
        (
          (response) =>
          {
            this.employee = response[0]["data"];
          },
          (error) =>
          {
            console.log("No Data Found" + error);
          }

        )
  }

  // readData()
  // {
  //   this.rs.readFile()
  //   .subscribe
  //       (
  //         (response) =>
  //         {
  //           this.weather = response[0]["data"];
  //         },
  //         (error) =>
  //         {
  //           console.log("File doesn't exist..." + error);
  //         }

  //       )
  // }

}
