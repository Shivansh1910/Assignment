import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { BrowserModule } from "@angular/platform-browser";
import { Routes, RouterModule } from "@angular/router";

import { IndexComponent } from "./pages/index/index.component";
import { ProfilepageComponent } from "./pages/examples/profilepage/profilepage.component";
import { RegisterpageComponent } from "./pages/examples/registerpage/registerpage.component";
import { LandingpageComponent } from "./pages/examples/landingpage/landingpage.component";
import { ManagerComponent } from "./final/manager/manager.component";
import { CandidateComponent } from "./final/candidate/candidate.component";
import { TestComponent } from "./final/test/test.component";
import { RegmComponent } from "./final/regm/regm.component";
import { RegcComponent } from "./final/regc/regc.component";
import { LogComponent } from "./final/log/log.component";
import { CertificateComponent } from "./final/certificate/certificate.component";

const routes: Routes = [
  { path: "", redirectTo: "log", pathMatch: "full" },
  { path: "home", component: IndexComponent },
  { path: "login", component: ProfilepageComponent },
  { path: "landing", component: LandingpageComponent },
  { path: "manager", component: ManagerComponent },
  { path: "candidate", component: CandidateComponent },
  { path: "main", component: RegisterpageComponent },
  { path: "test", component: TestComponent },
  { path: "regm", component: RegmComponent },
  { path: "regc", component: RegcComponent },
  { path: "log", component: LogComponent },
  { path: "certi", component: CertificateComponent },
];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes, {
      useHash: true
    })
  ],
  exports: []
})
export class AppRoutingModule { }
