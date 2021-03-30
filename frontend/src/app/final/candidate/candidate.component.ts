import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-candidate',
  templateUrl: './candidate.component.html',
  styleUrls: ['./candidate.component.scss']
})
export class CandidateComponent implements OnInit {
  isCollapsed = true;
  focus;
  focus1;
  focus2;
  name;
  email;
  manager;
  subject;
  discription;
  alpha;
  beta;
  gaama;
  event;
  temp;

  friends: [];
  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("profile-page");

    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })

    this.http.get<any>("http://127.0.0.1:8000/portal/detailm/", { headers: header }).subscribe(
      data => {
        console.log(data)
        this.alpha = data
      }
    )
    this.http.get<any>("http://127.0.0.1:8000/portal/detailc/", { headers: header }).subscribe(
      data => {
        console.log(data)
        this.beta = data
      }
    )
    this.http.get<any>("http://127.0.0.1:8000/portal/detailc1/", { headers: header }).subscribe(
      data => {
        console.log(data)
        this.gaama = data
      }
    )
  }
  submit() {
    console.log(this.name, this.email, this.manager, this.subject, this.discription)
    var url = "http://127.0.0.1:8000/portal/concern/";
    var body = new FormData();
    body.append('discription', this.discription)
    body.append('email', this.email)
    body.append('manager', this.manager)
    body.append('subject', this.subject)
    body.append('name', this.name)


    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        alert('submited request')
      }
    )

  };
  ngOnDestroy() {
    var url = "http://127.0.0.1:8000/portal/generate/";
    var body = new FormData()
    body.append('event', "nec")
    body.append('action', "delete")
    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })

    this.http.post<any>(url, body, { headers: header }).subscribe(
      data => {
        console.log(data)
        // this.temp = data
        // window.open(data);
      }
    )
  }

  send(button) {
    var url = "http://127.0.0.1:8000/portal/generate/";
    console.log(button);

    var body = new FormData()
    body.append('event', button)
    body.append('action', "generate")

    var header = new HttpHeaders({
      "Authorization": "Token " + localStorage.getItem('cp_token')
    })



    this.http.post<any>(url, body, { headers: header }).subscribe(
      data => {
        console.log(data)
        this.temp = data
        window.open(data);
      }
    )

  }

  logout() {
    localStorage.removeItem('cp_token')
    this.router.navigateByUrl('/log')
  }
}
