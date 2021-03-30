import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import noUiSlider from "nouislider";


declare var $: any;


@Component({
  selector: 'app-manager',
  templateUrl: './manager.component.html',
  styleUrls: ['./manager.component.scss']
})
export class ManagerComponent implements OnInit {
  isCollapsed = true;
  focus;
  focus1;
  focus2;

  // email;
  event1;
  event2;
  event3;
  certificate_name;
  img: File;
  is_discription;
  // discription;
  x;
  y;



  name;
  email;
  subject;
  discription;
  friends: [];


  temp;
  cname;

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("profile-page");
    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })

    this.http.get<any>("http://127.0.0.1:8000/portal/message/", { headers: header }).subscribe(
      data => {
        console.log(data)
        this.name = data

      }
    )

  }

  submit() {
    console.log(this.email, this.event1, this.event2, this.event3)
    var url = "http://127.0.0.1:8000/portal/control/";
    var body = new FormData();
    body.append('email', this.email)
    body.append('event1', this.event1)
    body.append('event2', this.event2)
    body.append('event3', this.event3)

    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        alert('created')

      }
    )

  };
  submitc() {
    console.log(this.certificate_name, this.img, this.x, this.y, this.discription, this.is_discription)
    var url = "http://127.0.0.1:8000/portal/sample/";
    var body = new FormData();
    body.append('certificate_name', this.certificate_name)
    body.append('img', this.img)
    body.append('x', this.x)
    body.append('y', this.y)
    body.append('is_discription', this.is_discription)
    body.append('discription', this.discription)

    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        alert('submitted img')

      }
    )

  }

  submitu() {
    console.log(this.cname, this.email)
    var url = "http://127.0.0.1:8000/portal/userupt/";
    var body = new FormData();
    body.append('email', this.email)
    body.append('name', this.cname)


    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        alert('success')

      }
    )

  }

  action() {
    var url = "http://127.0.0.1:8000/portal/delete/";
    console.log(this.temp);


    var body = new FormData()
    body.append('action', "delete")
    body.append('discription', this.temp)

    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
      }
    )

  }

  logout() {
    localStorage.removeItem('cp_token')
    this.router.navigateByUrl('/log')
  }
}