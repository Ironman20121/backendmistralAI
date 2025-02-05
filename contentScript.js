// contentScript.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getJobDetails") {
    const jobDetails = {
      title: getJobTitle(),
      company: getCompanyName(),
      description: getJobDescription(),
      location: getJobLocation(),
      url: window.location.href,
      date: new Date().toISOString()
    };
    sendResponse(jobDetails);
  }
  return true; // Keep the message channel open
});

function getJobTitle() {
  return document.querySelector('.jobs-details-top-card__job-title')?.innerText || 
         document.querySelector('.jobsearch-JobInfoHeader-title')?.innerText ||
         document.title.split(' - ')[0];
}

function getJobDescription() {
  return document.querySelector('.jobs-description__container')?.innerText || 
         document.querySelector('.jobsearch-jobDescriptionText')?.innerText ||
         '';
}

function getCompanyName() {
  return document.querySelector('.jobs-details-top-card__company-url')?.innerText || 
         document.querySelector('.jobsearch-CompanyInfoContainer a')?.innerText ||
         '';
}

function getJobLocation() {
  return document.querySelector('.jobs-details-top-card__exact-location')?.innerText || 
         document.querySelector('.jobsearch-JobMetadataHeader-item')?.innerText ||
         '';
}